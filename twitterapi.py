from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import _thread

import json
from pprint import pprint
import pdb
import time
import datetime
from time import mktime
from datetime import datetime

import sys, json, re, time

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, tweetDB):
        self.tweetDB = tweetDB

    def on_data(self, data):
        
        try:
            data = json.loads(data)
            tweet = {}
            tweet['tweet_id'] = str(data['id_str'])
            tweet['user_id'] = str(data['user']['id'])

            ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))

            tweet['time'] = ts
            tweet['content'] = re.sub('\s+', ' ', data['text'])
            self.tweetDB[tweet['tweet_id']] = tweet

            print("New tweet: " + data['user']['screen_name'])

        except:
            print("Unexpected error:", sys.exc_info())

    def on_error(self, status):
        print(status)

class TwitterAPI:

    def __init__(self):

        self.access_token = "61498960-FgeDUHKtBdJ9UMsqxGoZ7NnO3SotCWMy0rWA1JUV8"
        self.access_token_secret = "D5CTj5R7Z1Ut4a1KLH5lkPEP1c5bjsrHDIa6EumgHo"
        self.consumer_key = "AQvetavVmyibv81c4eavA"
        self.consumer_secret = "GDWmfSRcWeEwlX9N74JpghtqIovLpmS3usDZd2dGI"

        output = self.access_token+" "+self.access_token_secret+" "+self.consumer_key+" "+self.consumer_secret
        print('init TwitterAPI, credential: {}'.format(output))


    #mode true: geo, false not geo;
    def stream(self, tweetDB):

        #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener(tweetDB)
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = Stream(auth, l)

        #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
        #stream.filter(track=['python', 'javascript', 'ruby'])
        stream.filter(locations=[-87, 37, -84, 41], languages=['en'])

if __name__ == '__main__':
    api = TwitterAPI()
    tweetDB = {}
    api.stream(tweetDB)