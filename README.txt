A Context-Dependent Crowdsourcing Approach for Entity Recognition and Linking on Tweets

This is a course project at Purdue University taught by Prof.Alex Quinn.

Team member:
Jiawei Zhang (zhan1486@purdue.edu) and Jianqiao Liu (liu1274@purdue.edu)

External libraries required:
Tweepy
Flask
NLTK
pysqlite

Instructions:
1. In server.py, change the following line to direct to the location for NLTK data resources.
2. python server.py

Instructions on formatting the database:
1. cd ./data/
2. rm -rf db.sqlite
3. sqlite3 db.sqlite < schema.sql
4. cd ..

Code structure:
./data -- database file for tweets and entities
./static -- JS and css files for front-end interface
./templates -- html page for front-end interface

twitterapi.py -- a wrapper that captures the real-time Twitter stream within a geographic bounding box
server.py -- a flask server that provides web services and stores twitter and entities. A twitter api instance is created in the server class

db.py and prepare.py -- database operations in the back-end

More details on the implementation and code structure:

We store our test tweets into a TWEETS data table.

Graph/clustering process skeleton:
We use two data tables to record the entities and their links:

NPO table -- Unique, real record for each natural person/place/object, just like one's legal name. E.g. "Donald Trump". Each record in NPO would store all records in ETY that are sourced from it. We call each record in NPO table a "SRC".

ETY table -- Any entity machine/human detect from tweets, like one's nickname. Usually the mapping from record in ETY to record in NPO is a multiple-to-one mapping. E.g. "45", "DT" and "Orange Julius" could all exist in ETY table, and their "source" point to "Donald Trump" in NPO table. The "Donald Trump" may and may not exist in ETY (depends whether it appear in tweet). We call each record in ETY table a "DES".

When we detect a entity from tweets, we first check whether its include in the ETY table. 
1. If so, we get its "source" (SRC), go to NPO table, fetch all records sourced from SRC and display them in front end.
2. If not, the worker should create a record in NPO (DES). Then the worker should search through the NPO table with the most well-known name of the entity. This part could potentially be done through auto-complete or some smarter method.
	1. If there is such record in NPO (SRC), the worker should add the new record in ETY (DES) into SRC's list, and set DES's source as SRC (DES.source <- SRC).
	2. Otherwise, the worker also need to create a record in NPO (the SRC). The SRC has a name and a description. We strongly recommend the worker to use the most widely known name as SRC's name. The SRC's name is the unique keyword we define a person/place/object in our system. For current step, we can not avoid the duplication in NPO by machine, but we may potentially use crowd source to do this. The description of SRC could be a link to a Wikipedia webpage, or a piece of words written by the user.

Server-Client communication interface:

server -> client: (client() in server.py)
'tweets' contains a list of tweets
'links' contains a list of word mapping (can be empty)

client -> server: (submit() in server.py)
tweets and links are the same format as described above.

sample format:

tweets = 
 [{'user': 'U1', 'time': 'Mon, 17 Apr 2017 00:37:57 GMT', 'text': 'Hey there! I study at Purdue University.', 'id': 100, 'entity': [{'npo': 'Purdue University', 'ety':'boilerup', 'comment': '', 'isAuto': True, 'type': 'ORGANIZATION'}]}, {'user': 'U2', 'time': 'Mon, 17 Apr 2017 00:37:57 GMT', 'text': 'BoilerUp!', 'id': 101, 'entity': []}]

