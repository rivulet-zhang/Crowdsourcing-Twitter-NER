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

def clean_up_NPO_DB():
	db.query("DELETE FROM NPO where id > 0");

def clean_up_ETY_DB():
	db.query("DELETE FROM ETY where id > 0");

def clean_up_TWEETS_DB():
	db.query("DELETE FROM TWEETS where id > 0");

def prepare_NPO_DB():
	# GOOD:
	clean_up_NPO_DB()
	# For conversion 1
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Donald Trump", "PERSON", "https://en.wikipedia.org/wiki/Donald_Trump", "45"));

	# For conversion 2
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("The King of the Seven Kingdoms", "PERSON", "https://en.wikipedia.org/wiki/Daenerys_Targaryen", 
		"First of his name, King of the Andals and the First Men, Lord of the Seven Kingdoms, Protector of the Realm, "));
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Daenerys Targaryen", "PERSON", "https://en.wikipedia.org/wiki/Daenerys_Targaryen", 
		"The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons, "));

	# For conversion 3
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Indiana", "LOCATION", "https://en.wikipedia.org/wiki/Indiana", "Hoosiers"));

	# For conversion 4
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Academy Awards", "ORGANIZATION", "https://en.wikipedia.org/wiki/Oscar", "Oscar"));
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Manchester by the Sea", "OTHERS", "https://en.wikipedia.org/wiki/Manchester_by_the_Sea_(film)", "Manchester"));

	# For conversion 5
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("United Airlines", "ORGANIZATION", "https://en.wikipedia.org/wiki/Oscar", "United"));

	# For conversion 6
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Purdue University", "ORGANIZATION", "https://en.wikipedia.org/wiki/Purdue_University", "Boilermakers, Purdue"));

	# For conversion 7
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Kim Jong-un", "PERSON", "https://en.wikipedia.org/wiki/Purdue_University", "Great Successor"));

	# Additional information
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Mitch Daniels", "PERSON", "https://en.wikipedia.org/wiki/Mitch_Daniels", ""));
	db.query("INSERT INTO NPO (name, class, description, dest) values (?, ?, ?, ?)", ("Star Craft", "OTHERS", "https://en.wikipedia.org/wiki/StarCraft", ""));

def prepare_ETY_DB():
	# GOOD:
	clean_up_ETY_DB()
	# For conversion 1
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("45", "Donald Trump", "PERSON", "alex", "1:31 PM - 22 Apr 2017", "45 threatens to shut down government over funding for the wall that he promised Mexico would pay for.", 1, "False", ""));

	# For conversion 2
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("First of his name", "The King of the Seven Kingdoms", "PERSON", "Cain Snow", "2:48 PM - 22 Feb 2017", "First of his name. King of the Andals and the First Men, Lord of the Seven Kingdoms, and Protector of the Realm. Long may he reign.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("King of the Andals and the First Men", "The King of the Seven Kingdoms", "PERSON", "Cain Snow", "2:48 PM - 22 Feb 2017", "First of his name. King of the Andals and the First Men, Lord of the Seven Kingdoms, and Protector of the Realm. Long may he reign.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Lord of the Seven Kingdoms", "The King of the Seven Kingdoms", "PERSON", "Cain Snow", "2:48 PM - 22 Feb 2017", "First of his name. King of the Andals and the First Men, Lord of the Seven Kingdoms, and Protector of the Realm. Long may he reign.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Protector of the Realm", "The King of the Seven Kingdoms", "PERSON", "Cain Snow", "2:48 PM - 22 Feb 2017", "First of his name. King of the Andals and the First Men, Lord of the Seven Kingdoms, and Protector of the Realm. Long may he reign.", 2, "False", ""));

	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("The Unburnt Queen of the Andals", "Daenerys Targaryen", "PERSON", "mat morgan", "4:51 PM - 22 Feb 2017", "The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Queen of Meereen", "Daenerys Targaryen", "PERSON", "mat morgan", "4:51 PM - 22 Feb 2017", "The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Khaleesi of the Great Grass Sea", "Daenerys Targaryen", "PERSON", "mat morgan", "4:51 PM - 22 Feb 2017", "The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Breaker of Chains", "Daenerys Targaryen", "PERSON", "mat morgan", "4:51 PM - 22 Feb 2017", "The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons.", 2, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Mother of Dragons", "Daenerys Targaryen", "PERSON", "mat morgan", "4:51 PM - 22 Feb 2017", "The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons.", 2, "False", ""));

	# For conversion 3
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Hoosiers", "Indiana", "LOCATION", "Not Jerry Tipton", "5:19 PM - 21 Apr 2017", "Indiana fans celebrating the Hoosiers' most recent national championship.", 3, "False", ""));

	# For conversion 4
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Oscar", "Academy Awards", "ORGANIZATION", "yung da bejar", "10:50 PM - 27 Mar 2017", "I liked it overall but it felt very \"Oscar nominated movie\". will checkout Manchester soon ", 4, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Manchester", "Manchester by the Sea", "OTHERS", "yung da bejar", "10:50 PM - 27 Mar 2017", "I liked it overall but it felt very \"Oscar nominated movie\". will checkout Manchester soon ", 4, "False", ""));

	# For conversion 5
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("United", "United Airlines", "ORGANIZATION", "Hazha", "3:06 PM - 19 Apr 2017", "United #Overbooked hazha.com/yay/xGg", 5, "False", ""));

	# For conversion 6
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Boilermakers", "Purdue University", "ORGANIZATION", "Purdue Basketball", "7:01 PM - 8 Apr 2017", "SEE YA!! Logan Poisall goes big fly to left field. #Purdue's 2nd 2-run blast tonight. It's 6-0 #Boilermakers as they've jumped all over IU.", 6, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Purdue", "Purdue University", "ORGANIZATION", "Purdue Basketball", "7:01 PM - 8 Apr 2017", "SEE YA!! Logan Poisall goes big fly to left field. #Purdue's 2nd 2-run blast tonight. It's 6-0 #Boilermakers as they've jumped all over IU.", 6, "False", ""));

	# For conversion 7
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
		("Great Successor", "Kim Jong-un", "PERSON", "Kevin-Economy&Beyond", "4:23 AM - 18 Aug 2016", "This will not amuse The Great Successor. BBC News -China to restrict North Korea's Air Koryo after emergency landing", 7, "False", ""));

	# Additional information
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", ("Orange Julius", "Donald Trump", "PERSON", "alex", "201704010102", "is Orange Julius a good man?", 0, "False", ""));
	db.query("INSERT INTO ETY (name, source, class, user, tweet_time, context, convers_id, isAuto, comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", ("BoilerUp", "Purdue University", "ORGANIZATION", "alex", "201704010103", 
		"We come from Purdue University! We are Boiler Makers!", 0, "False", ""));

def prepare_TWEETS_DB():
	# GOOD:
	clean_up_TWEETS_DB()
#Conversation 1
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)",
		                         ("Nick Decaro", 
		                         	"1:31 PM - 22 Apr 2017", 
		                         	"45 threatens to shut down government over funding for the wall that he promised Mexico would pay for.",
		                         	1));
#Conversation 2
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("Cain Snow", 
		                         	"2:48 PM - 22 Feb 2017", 
		                         	"First of his name. King of the Andals and the First Men, Lord of the Seven Kingdoms, and Protector of the Realm. Long may he reign.",
		                         	2));
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("mat morgan", 
		                         	"4:51 PM - 22 Feb 2017", 
		                         	"The Unburnt Queen of the Andals, Queen of Meereen, Khaleesi of the Great Grass Sea, Breaker of Chains, Mother of Dragons.",
		                         	2));
#Conversation 3
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("Not Jerry Tipton", 
		                         	"5:19 PM - 21 Apr 2017", 
		                         	"Indiana fans celebrating the Hoosiers' most recent national championship.",
		                         	3));
#Conversation 4
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("yung da bejar", 
		                         	"10:50 PM - 27 Mar 2017", 
		                         	"I liked it overall but it felt very \"Oscar nominated movie\". will checkout Manchester soon ",  
		                         	4));
#Conversation 5
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("Hazha", 
		                         	"3:06 PM - 19 Apr 2017", 
		                         	"United #Overbooked hazha.com/yay/xGg",  
		                         	5));
#Conversation 6
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("Purdue Basketball", 
		                         	"7:01 PM - 8 Apr 2017", 
		                         	"SEE YA!! Logan Poisall goes big fly to left field. #Purdue's 2nd 2-run blast tonight. It's 6-0 #Boilermakers as they've jumped all over IU.",  
		                         	6));
#Conversation 7
	db.query("INSERT INTO TWEETS (user, tweet_time, content, convers_id) values (?, ?, ?, ?)", 
		                         ("Kevin-Economy&Beyond", 
		                         	"4:23 AM - 18 Aug 2016", 
		                         	"This will not amuse The Great Successor. BBC News -China to restrict North Korea's Air Koryo after emergency landing",  
		                         	7));

#if __name__=="__main__":
def test_DB():
	with app.app_context():
		prepare_NPO_DB()
		prepare_ETY_DB()
		prepare_TWEETS_DB()

#		rows = db.query("select * from NPO")
#		print rows
#		rows = db.query("select * from ETY")
#		print rows
#		rows = db.query("select * from TWEETS")
#		print rows
		
		print("All is well!")



