#---Imports--#
import tweepy
import time
from credentials import *
from train_reply import *
import image_seach_engine as posting_bot

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# --Daily Post---#
def posting_bot():
    api = tweepy.API(auth)

    #---random generation---#
    train_words = search_words
    #train_words = ['trains','locomotive','railway','railwayphotography','steam locomotive', 'CSX','#trains','#locomotive','#railway','#railwayphotography','#steam locomotive']
    word_type = random.choice(train_words)
    random_number = random.randint(1,100)

    #---Choose parameters---#
    response().download(f'{word_type} {random_number}', 1)
    urltxt = response().urls(f'{word_type} {random_number}', 1)

    #---Fixing URL---#
    bad_chars = ['[', ']']
    urltxt = ''.join(i for i in urltxt if not i in bad_chars)
    #print(str(urltxt))

    #---File location---#
    global train_img
    global train_text
    train_img = 'simple_images/trainpic.jpg'
    train_text = (f' Source: {urltxt} \n#trains #locomotive #railroad #railway #train #railfan #railroads')

    #---Post---#
    print(f'The search was {word_type} {random_number}')
    api.update_with_media(train_img, train_text)