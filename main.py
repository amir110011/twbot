import tweepy
from info import *
from menu import selected
from functions import new_twitt, logs
# autenticat to twitter

# read the keys from info.py
# autenticate to twitter
# with client
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
# with api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# ===========================================================

try:
    api.verify_credentials()
    print("Authentication Successful\n")
except:
    print("Authentication Error\n")


# menu
if selected == '1':
    # Create Tweet
    try:
        text = new_twitt()
        response = client.create_tweet(text=text)
        logs(f'twitt created ( {text} )')
        print("$ TWBOT SAYS:\n Message: Tweet created")
    except Exception as error:
        error_string = str(error)
        logs(f'{error_string}')
        print("$ TWBOT SAYS:\nError: {}".format(error_string))

elif selected == '2':
    # the screen name of the user
    screen_name = input("Enter the user name: ")
    # fetching the user
    user = api.get_user(screen_name=f"{screen_name}")
    # fetching the ID
    print(f"""
        $ TWBOT SAYS:
    =======================================
        The ID: {user.id_str}
        The name: {user.name}
        followers: {user.followers_count}
        following: {user.friends_count}
    =======================================
    """)

elif selected == '0':
    print("Exiting")
    exit()
else:
    print("Error: invalid option")
