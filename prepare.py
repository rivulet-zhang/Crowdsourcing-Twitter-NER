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

def reset_NPO_DB():
		# GOOD:
		db.query("DELETE FROM NPO where id > 0");
		db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Donald Trump", "PERSON", "https://en.wikipedia.org/wiki/Donald_Trump", "None"));
		db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Purdue University", "ORGANIZATION", "https://en.wikipedia.org/wiki/Purdue_University", "None"));
		db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Mitch Daniels", "PERSON", "https://en.wikipedia.org/wiki/Mitch_Daniels", "None"));
		db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Star Craft", "Object", "https://en.wikipedia.org/wiki/StarCraft", "None"));

def reset_ETY_DB():
		# GOOD:
		db.query("DELETE FROM ETY where id > 0");
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, convers_id, isAuto) values (?, ?, ?, ?, ?, ?, ?)", ("45", "Donald Trump", "alex", "201704010100", "is 45 a good man?", 0, "False"));
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, convers_id, isAuto) values (?, ?, ?, ?, ?, ?, ?)", ("DT", "Donald Trump", "alex", "201704010101", "is DT a good man?", 0, "False"));
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, convers_id, isAuto) values (?, ?, ?, ?, ?, ?, ?)", ("Orange Julius", "Donald Trump", "alex", "201704010102", "is Orange Julius a good man?", 0, "False"));
		db.query("INSERT INTO ETY (name, source, user, tweet_time, context, convers_id, isAuto) values (?, ?, ?, ?, ?, ?, ?)", ("Boiler Maker", "Purdue University", "alex", "201704010103", 
			"We come from Purdue University! We are Boiler Makers!", 0, "False"));

def reset_TWEETS_DB():
		# GOOD:
		db.query("DELETE FROM TWEETS where id > 0");
#Conversation 1
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("jiawei", 
			                         	datetime.datetime.now(), 
			                         	"Hi, I study at Purdue University.",
			                         	1));
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("jianqiao", 
			                         	datetime.datetime.now(), 
			                         	"Boilerup! Is it in Indiana?",
			                         	1));
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("jiawei", 
			                         	datetime.datetime.now(), 
			                         	"Yup, the Hoosier State.", 
			                         	1));
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("jianqiao", 
			                         	datetime.datetime.now(), 
			                         	"Have you ever seen the RV-1 of your president?",  
			                         	1));
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("jiawei", 
			                         	datetime.datetime.now(), 
			                         	"Sure, that's a very fancy RV!", 
			                         	1));
#Conversation 2
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("A", 
			                         	datetime.datetime.now(), 
			                         	"I cannot believe 45 has won the election!",
			                         	2));
		db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
			                         ("B", 
			                         	datetime.datetime.now(), 
			                         	"Neither I. Just look at what these rednecks do!",  
			                         	2));

#if __name__=="__main__":
def test_DB():
	with app.app_context():
		reset_NPO_DB()
		reset_ETY_DB()
		reset_TWEETS_DB()

#		rows = db.query("select * from NPO")
#		print rows
#		rows = db.query("select * from ETY")
#		print rows
#		rows = db.query("select * from TWEETS")
#		print rows
		
		print("All is well!")



