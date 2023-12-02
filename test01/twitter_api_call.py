import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
# print(os.environ)


# Access the environment variables
twitter_api_key = os.environ.get('twitter_api_key')
twitter_api_secret = os.environ.get('twitter_api_secret')
twitter_access_token = os.environ.get('twitter_access_token')
twitter_access_token_secret = os.environ.get('twitter_access_token_secret')
# print(twitter_access_token)

# Authenticate to Twitter
auth = tweepy.OAuthHandler('SOAnUkC7vMvw7ykkvtVxq4QSR', str(twitter_api_secret))
auth.set_access_token(str(twitter_access_token), str(twitter_access_token_secret))

# # Create API object
api = tweepy.API(auth)

user = api.get_user(screen_name="ski_traffic_bot")
print(user.screen_name)
