# (c) Copyright 2016  Jiawei Zhang and Jianqiao Liu - MIT License
from __future__ import division, unicode_literals 
import flask
import config, db
#from twitterapi import TwitterAPI

import threading
from threading import Thread

import datetime

app = flask.Flask(__name__, static_url_path='/static') # Create application
app.config.from_object(config)                         # Currently has no real effect



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

def prepare_NPO_DB():
	with app.app_context():
		# GOOD:
		db.query("INSERT INTO NPO (name, dest) values (?, ?)", ("Donald Trump", "None"));
		db.query("INSERT INTO NPO (name, dest) values (?, ?)", ("Purdue University", "None"));
		db.query("INSERT INTO NPO (name, dest) values (?, ?)", ("Mitch Daniels", "None"));
		db.query("INSERT INTO NPO (name, dest) values (?, ?)", ("Star Craft", "None"));

def prepare_ETY_DB():
	with app.app_context():
		# GOOD:
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, isAuto) values (?, ?, ?, ?, ?, ?)", ("45", "Donald Trump", "alex", "201704010100", "is 45 a good man?", "False"));
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, isAuto) values (?, ?, ?, ?, ?, ?)", ("DT", "Donald Trump", "alex", "201704010101", "is DT a good man?", "False"));
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, isAuto) values (?, ?, ?, ?, ?, ?)", ("Orange Julius", "Donald Trump", "alex", "201704010102", "is Orange Julius a good man?", "False"));


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
#	test_add_tweet()
	prepare_NPO_DB()
	prepare_ETY_DB()
#	app.run(host="127.0.0.1", port=8080, debug=False, use_debugger=False, use_evalex=False)
	print("All is well!")