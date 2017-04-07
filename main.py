# (c) Copyright 2016  Jiawei Zhang and Jianqiao Liu - MIT License
from __future__ import division, unicode_literals 
import flask
from twitterapi import TwitterAPI

import threading
from threading import Thread

app = flask.Flask(__name__)

# global variable to store real-time tweets
tweetDB = {}

def start_twitter_api():
	api = TwitterAPI()
	api.stream(tweetDB)


# ajax call initiated by client to get a new tweet from server
@app.route('/gettweet', methods=['GET'])
def getTweet():
	return ""


# default page for client html
@app.route('/')
def client():
	return flask.render_template("client.html")

if __name__=="__main__":
	# run server and twitter api concurrently
	Thread(target = start_twitter_api).start()
	app.run(host="127.0.0.1", port=8080, debug=False, use_debugger=False, use_evalex=False)