A course project for Crowd-Powered Systems (in progress)

Team member:
Jiawei Zhang and Jianqiao Liu

External libraries required:
Tweepy

Instruction:
python server.py

Code structure:
twitterapi.py -- a wrapper that captures the real-time Twitter stream within a geographic bounding box.
server.py -- a flask server that provides web services and stores twitter and entities. A twitter api instance is created in the server class.
templates/client.html -- a front end interface for workers to tag entities in Twitter messages.



Graph process skeleton:
We use two databases to record the entities and their links:

NPO database -- Unique, real record for each natural person/place/object, just like one's legal name. E.g. "Donald Trump". Each record in NPO would store all records in ETY that are sourced from it. We call each record in NPO database a "SRC".

ETY database -- Any entity machine/human detect from tweets, like one's nickname. Usually the mapping from record in ETY to record in NPO is a multiple-to-one mapping. E.g. "45", "DT" and "Orange Julius" could all exist in ETY database, and their "source" point to "Donald Trump" in NPO database. The "Donald Trump" may and may not exist in ETY (depends whether it appear in tweet). We call each record in ETY database a "DES".

When we detect a entity from tweets, we first check whether its include in the ETY database. 
1. If so, we get its "source" (SRC), go to NPO database, fetch all records sourced from SRC and display them in front end.
2. If not, the worker should create a record in NPO (DES). Then the worker should search through the NPO database with the most well-known name of the entity. This part could potentially be done through auto-complete or some smarter method.
	1. If there is such record in NPO (SRC), the worker should add the new record in ETY (DES) into SRC's list, and set DES's source as SRC (DES.source = SRC).
	2. Otherwise, the worker also need to create a record in NPO (the SRC). The SRC has a name and a description. We strongly recommend the worker to use the most widely known name as SRC's name. The SRC's name is the unique keyword we define a person/place/object in our system. For current step, we can not avoid the duplication in NPO by machine, but we may potentially use crowd source to do this. The description of SRC could be a link to a Wikipedia webpage, or a piece of words written by the user.
