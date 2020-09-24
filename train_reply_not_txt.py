import tweepy
import time
import random
from credentials import *
from train_search_words import search_words
from image_seach_engine import image_seacher_code as response

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# FILE_NAME = 'last_seen.txt'
#
# def retrieve_last_seen_id(FILE_NAME):
#     f_read = open(FILE_NAME, 'r')
#     last_seen_id = int(f_read.read().strip())
#     f_read.close()
#     return last_seen_id
#
# def store_last_seen_id(FILE_NAME, last_seen_id):
#     f_write = open(FILE_NAME, 'w')
#     f_write.write(str(last_seen_id))
#     f_write.close()
#     return

def bot_instructions():
    print('Waiting for mentions...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        if not mention:
            return
        print(str(mention.id) + '-' + mention.full_text, flush=True)
        print('Found @Daily Train Post', flush=True)
        print('fav-ing and retweeting tweet...', flush=True)
        api.create_favorite(mention.id)
        api.retweet(mention.id)

def bot_reply():
    bot_instructions()



	# tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
	# for tweet in reversed(tweets):
	# 	print(str(tweet.id) + '-' + tweet.full_text)
	#
	# 	# ---random generation---#
	# 	word_type = random.choice(search_words)
	# 	random_number = random.randint(1, 100)
    #
	# 	# ---Choose parameters---#
	# 	response().download(f'{word_type} {random_number}', 1)
	# 	urltxt = response().urls(f'{word_type} {random_number}', 1)
    #
	# 	# ---Fixing URL---#
	# 	bad_chars = ['[', ']']
	# 	urltxt = ''.join(i for i in urltxt if not i in bad_chars)
	# 	# print(str(urltxt))
    #
	# 	# ---File location---#
	# 	train_img = 'simple_images/trainpic.jpg'
	# 	status = ("@" + str(tweet.user.screen_name) + ' Choo! Choo! Here is a train just for you!')
	# 	in_reply_to_status_id = tweet.id
	# 	api.update_with_media(train_img, status, in_reply_to_status_id=in_reply_to_status_id)
	# 	api.create_favorite(tweet.id)
	# 	#api.retweet(tweet.id)
	# 	store_last_seen(FILE_NAME, tweet.id)
	# 	print(f'The search was {word_type} {random_number}')
