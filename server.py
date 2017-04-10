# (c) Copyright 2016  Jiawei Zhang and Jianqiao Liu - MIT License
from __future__ import division, unicode_literals 
import flask
from twitterapi import TwitterAPI

import threading
from threading import Thread

import datetime

app = flask.Flask(__name__, static_url_path='/static') # Create application

# global variable to store real-time tweets
tweetDB = {}

# start twitter api to collect realtime tweets
def start_twitter_api():
	api = TwitterAPI()
	api.stream(tweetDB)


# entity type: org -> organization, psn -> person, loc -> location
def test_add_tweet():
	tweet = {}
	tweet['id'] = 1234567890
	tweet['user'] = 'jiawei'
	tweet['time'] = datetime.datetime.now()
	tweet['text'] = 'I study at Purdue University. The president of the university is Mitch Daniels.'
	tweet['entity'] = []
	tweet['entity'].append({'type':'org', 'term':'Purdue University', 'isAuto':True})
	tweet['entity'].append({'type':'psn', 'term':'Mitch Daniels', 'isAuto':True})
	tweetDB[tweet['id']] = tweet

# # ajax call initiated by client to get a new tweet from server
# @app.route('/gettweet', methods=['GET'])
# def getTweet():
# 	return ""

def get_a_tweet():
	tweets = list(tweetDB.values());
	if len(tweets) <= 0:
		print("not enough tweets")
	else:
		return tweets[0]

# default page for client html
@app.route('/')
def client():

	tweet = get_a_tweet();
	return flask.render_template("client.html", tweet=tweet)

if __name__=="__main__":
	# run server and twitter api concurrently
	# Thread(target = start_twitter_api).start()
	test_add_tweet()
	app.run(host="127.0.0.1", port=8080, debug=False, use_debugger=False, use_evalex=False)