# (c) Copyright 2016  Jiawei Zhang and Jianqiao Liu - MIT License
from __future__ import division, unicode_literals 
from sys import platform
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
if platform == "darwin":
	nltk.data.path.append("/Users/jianqiaoliu/Downloads/nltk_data")
else:
	nltk.data.path.append("E:/nltk_data")

# global variable to store real-time tweets
tweetDB = {}
_g_conversation_counter = 0

# When the flag is set to 1, we will use our complete database to show the full result
# Otherwise, we just show the machine result and let the crowd do the recognize & link entities
_g_use_Crowd_DB = 1			

# Package the entity information for front-end display
def extract_entity_names(t, found_entities):
    entity_names = []
    if hasattr(t, 'label') and t.label :
        if t.label() == 'PERSON' or t.label() == 'ORGANIZATION' or t.label() == 'LOCATION':
    		name = ' '.join([child[0] for child in t])
    		found = False;
    		# Check whether this entity has already been included by other crowd-recognized entity. If included, drop this entity
    		# We set human priority higher than machines
    		for entity in found_entities:
    			if entity.find(name) != -1:
    				found = True
    				break;
    		if found == False:
    			entity_names.append({'term':' '.join([child[0] for child in t]), 'type':t.label(), 'isAuto':True, 'comment':''})
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child, found_entities))

    return entity_names

# Each time we get a new tweet conversation
def get_conversation_from_DB():
	global _g_conversation_counter
	# In our evaluation, there are only 7 tweets in total. We repeated process them (from 1 to 7)
	_g_conversation_counter = (_g_conversation_counter + 1) % 8
#	_g_conversation_counter = 1
	sql = "SELECT * from TWEETS WHERE convers_id=%d" % (_g_conversation_counter)
	parameters=()
	conn = db.get_connection()
	execute = conn.execute(sql, parameters)
	rows = execute.fetchall()

	tweets = []
	for row in rows:
		t = {}
		entity_names = []
		for idx, col in enumerate(execute.description):
			t[col[0]] = row[idx]

		# We search our own database to find recognized entities
		existed_entities = db.query("select * from ETY")
		found_entities = []
		for entity_row in existed_entities:
			# we direct access the name of entity by the index, 0 means the id, 1 means the name, 2 means the source, 3 for type, 9 for comment
			entity = entity_row[1]
			if t['content'].find(entity) != -1:
				entity_record = []
				entity_record.append({'term':entity_row[1], 'type':entity_row[3], 'isAuto':True, 'comment':entity_row[9]})
				entity_names.extend(entity_record)
				found_entities.append(entity_row[1])

		# We use the "NLTK" tool kit to automatically process entities
		sentences = nltk.sent_tokenize(t['content'])
		tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
		tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
		chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)
		for tree in chunked_sentences:
		    entity_names.extend(extract_entity_names(tree, found_entities))

		t['entity'] = entity_names
		# print(entity_names)
		tweets.append(t)

#	print(tweets)
	return tweets

def get_link_from_DB(tweets):
	links = []
	for tweet in tweets:
		if len(tweet['entity']) != 0:
			for entity in tweet['entity']:
				# We search the entity link from the ETY table
				# We assume the standard name of NPO has already been handled by machine, or it's well-known, so we ignore them
				_row = db.query("SELECT * from ETY WHERE name=\'%s\'" % entity['term'])
				if len(_row) != 0:
					comment = {'user':_row[0][4], 'context':_row[0][6], 'comment':_row[0][9]}
					comment = json.dumps(comment)
					links.append({'npo':_row[0][2],'ety':entity['term'],'comment':comment})

#	print('*****links begin*****')
#	print(links)
#	print('*****links end*****')
	return links

# default page for client html
@app.route('/')
def client():
	tweets = get_conversation_from_DB();
	links = get_link_from_DB(tweets)
	return flask.render_template("client.html", tweets=tweets, links=links)

@app.route('/submit', methods=['POST'])
def submit():

	rst = flask.request.form
	tweets = json.loads(rst['tweetsResult'])['tweets']
	# links = json.loads(rst['linksResult'])['links']

	for tweet in tweets:
		if len(tweet['entity']) != 0:
			for entity in tweet['entity']:
				if 'npo' in entity:
					npo_row = db.query("SELECT * from NPO WHERE name=\'%s\'" % entity['npo'])
					# If record could not be found from NPO table, create a new record
					if len(npo_row) == 0:
						db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", 
							(entity['npo'], entity['type'], "https://en.wikipedia.org/wiki/" + entity['npo'], entity['ety']));
					# Else, update existing record
					else:
						new_dest = npo_row[0][4] + ", " + entity['ety']
						sql = "UPDATE NPO SET dest=%s WHERE name=%s" % (new_dest, entity['npo'])
						db.query(sql);

					# Insert a new entity into ETY table
					ety_row = db.query("SELECT * from ETY WHERE name=\'%s\'" % entity['ety'])
					if len(ety_row) == 0:
						db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) " +
						 " values (?, ?, ?, ?, ?, ?, ?, ?, ?)", (entity['ety'], entity['npo'], entity['type'], tweet['user'], "", tweet['content'], 0, "False", entity['comment']));

#	rows = db.query("select * from NPO")
	# print rows
#	rows = db.query("select * from ETY")
	# print rows
	return "Answer received"


if __name__=="__main__":
	with app.app_context():
		if _g_use_Crowd_DB == 1:
			prepare.test_DB()
		else:
			prepare.clean_up_NPO_DB()
			prepare.clean_up_ETY_DB()
			prepare.prepare_TWEETS_DB()
		app.run(host="127.0.0.1", port=8080, debug=False, use_debugger=False, use_evalex=False)

