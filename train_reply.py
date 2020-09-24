import tweepy
import time
import random
from credentials import *
from train_search_words import search_words
from image_seach_engine import image_seacher_code as response

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def bot_instructions():
    print('Waiting for mentions...')
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        print(str(tweet.id) + '-' + tweet.full_text)
        print('Found @Daily Train Post', flush=True)
        print('fav-ing and retweeting tweet...', flush=True)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)

def bot_reply():
    bot_instructions()

