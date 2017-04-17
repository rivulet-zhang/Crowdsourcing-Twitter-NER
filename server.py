# (c) Copyright 2016  Jiawei Zhang and Jianqiao Liu - MIT License
from __future__ import division, unicode_literals 
import flask
import prepare
#from twitterapi import TwitterAPI
import json
import pdb

import threading
from threading import Thread

import datetime

app = flask.Flask(__name__, static_url_path='/static') # Create application

# global variable to store real-time tweets
tweetDB = {}

# start twitter api to collect realtime tweets
# def start_twitter_api():
# 	api = TwitterAPI()
# 	api.stream(tweetDB)


# entity type: org -> organization, psn -> person, loc -> location
def test_add_tweet():
	tweets = []
	t1 = {}
	t1['id'] = 100
	t1['user'] = 'U1'
	t1['time'] = datetime.datetime.now()
	t1['text'] = 'Hey there! I study at Purdue University.'
	t1['entity'] = []
	t1['entity'].append({'type':'org', 'term':'Purdue University', 'isAuto':True, 'comment':''})

	t2 = {}
	t2['id'] = 101
	t2['user'] = 'U2'
	t2['time'] = datetime.datetime.now()
	t2['text'] = 'BoilerUp!'
	t2['entity'] = []

	tweets.append(t1);
	tweets.append(t2);

	conversationId = 1

	tweetDB[conversationId] = tweets


# # ajax call initiated by client to get a new tweet from server
# @app.route('/gettweet', methods=['GET'])
# def getTweet():
# 	return ""

def get_conversation():
	tweets = list(tweetDB.values());
	if len(tweets) <= 0:
		print("not enough tweets")
	else:
		return tweets[0]

def get_link(tweets):
	return [{'term1':'Purdue University','term2':'BoilerUp','comment':''}]

# default page for client html
@app.route('/')
def client():

	tweets = get_conversation();
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
	# run server and twitter api concurrently
	# Thread(target = start_twitter_api).start()
	test_add_tweet()
	prepare.test_DB()
	app.run(host="127.0.0.1", port=8080, debug=False, use_debugger=False, use_evalex=False)