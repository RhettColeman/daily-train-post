#---Imports--#
import tweepy
import time
from credentials import *
from train_posting_bot import*

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


#---train_reply---#
while True:
    posting_bot()
    time.sleep(60 * 60 * 24)
