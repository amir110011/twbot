import tweepy
from info import *
# autenticat to twitter

# read the keys from info.py
# autenticate to twitter
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Create Tweet
try:
    response = client.create_tweet(text="This Tweet was Tweeted using Tweepy and Twitter API v2!")
except:
    print("Error: Tweet not created")