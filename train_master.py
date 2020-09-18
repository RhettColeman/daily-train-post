#---Imports--#
import tweepy
import time
from credentials import *
from train_reply import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


#---train_reply---#
file = open("last_seen.txt","r+")
f.seek(0)
file.truncate()
bot_reply()

while True:
	bot_reply()
	time.sleep(30)
