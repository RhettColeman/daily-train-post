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

def bot_reply():
	print('Wating for mentions...')
	tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
	for tweet in reversed(tweets):
		print(str(tweet.id) + '-' + tweet.full_text)
		
		# ---random generation---#
		word_type = random.choice(search_words)
		random_number = random.randint(1, 100)

		# ---Choose parameters---#
		response().download(f'{word_type} {random_number}', 1)
		urltxt = response().urls(f'{word_type} {random_number}', 1)

		# ---Fixing URL---#
		bad_chars = ['[', ']']
		urltxt = ''.join(i for i in urltxt if not i in bad_chars)
		# print(str(urltxt))

		# ---File location---#
		train_img = 'simple_images/trainpic.jpg'
		status = ("@" + str(tweet.user.screen_name) + ' Choo! Choo! Here is a train just for you!')
		in_reply_to_status_id = tweet.id
		api.update_with_media(train_img, status, in_reply_to_status_id=in_reply_to_status_id)
		api.create_favorite(tweet.id)
		#api.retweet(tweet.id)
		store_last_seen(FILE_NAME, tweet.id)
		print(f'The search was {word_type} {random_number}')

while True:
    bot_reply()
    time.sleep(30)