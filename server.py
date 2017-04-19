# (c) Copyright 2016  Jiawei Zhang and Jianqiao Liu - MIT License
from __future__ import division, unicode_literals 
import flask
import config, db, prepare
#from twitterapi import TwitterAPI
import json
import pdb
import nltk

import threading
from threading import Thread

import datetime

app = flask.Flask(__name__, static_url_path='/static') # Create application
app.config.from_object(config)                         # Currently has no real effect
nltk.data.path.append("/Users/jianqiaoliu/Downloads/nltk_data")

# global variable to store real-time tweets
tweetDB = {}
_g_conversation_counter = 0

# start twitter api to collect realtime tweets
# def start_twitter_api():
# 	api = TwitterAPI()
# 	api.stream(tweetDB)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'PERSON' or t.label() == 'ORGANIZATION' or t.label() == 'LOCATION':
            # pdb.set_trace()
            entity_names.append([' '.join([child[0] for child in t]), t.label()])
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names


# entity type: org -> organization, psn -> person, loc -> location
def test_add_tweet():
	tweets = []
	t1 = {}
	t1['id'] = 100
	t1['user'] = 'U1'
	t1['tweet_time'] = datetime.datetime.now()
	t1['content'] = 'Hey there! I study at Purdue University.'
	t1['entity'] = []
	t1['entity'].append({'type':'org', 'term':'Purdue University', 'isAuto':True, 'comment':''})

	t2 = {}
	t2['id'] = 101
	t2['user'] = 'U2'
	t2['tweet_time'] = datetime.datetime.now()
	t2['content'] = 'BoilerUp!'
	t2['entity'] = []

	tweets.append(t1);
	tweets.append(t2);

	conversationId = 1

	tweetDB[conversationId] = tweets
	print type(t2['entity'])


# # ajax call initiated by client to get a new tweet from server
# @app.route('/gettweet', methods=['GET'])
# def getTweet():
# 	return ""

def get_conversation():
	tweets = list(tweetDB.values());
	print "All is well"
	print tweets[0]
	if len(tweets) <= 0:
		print("not enough tweets")
	else:
		return tweets[0]

def get_conversion_from_DB():
	global _g_conversation_counter
	_g_conversation_counter = _g_conversation_counter + 1
	sql = "SELECT * from TWEETS WHERE convers_id=%d" % _g_conversation_counter
	parameters=()
	conn = db.get_connection()
	execute = conn.execute(sql, parameters)
	rows = execute.fetchall()

	tweets = []
	for row in rows:
		t = {}
		for idx, col in enumerate(execute.description):
			t[col[0]] = row[idx]

		entity_names = []
		sentences = nltk.sent_tokenize(t['content'])
		tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
		tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
		chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)
		for tree in chunked_sentences:
		    entity_names.extend(extract_entity_names(tree))

		t['entity'] = entity_names
		tweets.append(t)
	return tweets

def get_link(tweets):
	return [{'term1':'Purdue University','term2':'BoilerUp','comment':''}]

# default page for client html
@app.route('/')
def client():

	tweets = get_conversion_from_DB();
	links = get_link(tweets)
	return flask.render_template("client.html", tweets=tweets, links=links)

@app.route('/submit', methods=['POST'])
def submit():

	rst = flask.request.form

	tweets = json.loads(rst['tweetsResult'])['tweets']
	links = json.loads(rst['linksResult'])['links']

	print("tweets: ", tweets)
	print("links: ", links)

	return "Answer received"


if __name__=="__main__":
	with app.app_context():
		# run server and twitter api concurrently
		# Thread(target = start_twitter_api).start()
		test_add_tweet()
		prepare.test_DB()
#		get_conversation()
		get_conversion_from_DB()
		app.run(host="127.0.0.1", port=8080, debug=False, use_debugger=False, use_evalex=False)