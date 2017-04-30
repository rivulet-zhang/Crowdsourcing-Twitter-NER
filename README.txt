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