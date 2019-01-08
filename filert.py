from credentials import *
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q= '#HarryPotter').items(10):
    try:
        tweet.retweet()
        print('successful')
        sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


