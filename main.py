import tweepy
from info import *
from menu import selected
from defs import new_twitt, logs
# autenticat to twitter

# read the keys from info.py
# autenticate to twitter
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

if selected == '1':
    # Create Tweet
    try:
        text = new_twitt()
        response = client.create_tweet(text=text)
        logs(f'twitt created ( {text} )')
        print("Message: Tweet created")

    except Exception as error:
        error_string = str(error)
        logs(f'{error_string}')
        print("Error: {}".format(error_string))
else:
    print("Error: invalid option")