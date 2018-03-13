import tweepy
from textblob import TextBlob

# Accessing and authenticating with Twitter API

consumer_key = 'vKCltNIfzwHag1LYVCnUbrLdb'
consumer_secret = 'topqI8HA6NtTgwQalhTnaF0ZFuJNJZMbUaljIAzwg8N48AKbSy'

access_token = '2333876111-W9OGoF0aTKjwBTBPQMsY1dVg0aANCxJ696SFC9e'
access_token_secret = 'E4bu7wK2VIkNEJNNeh46bwuuDQdgfHpyT7c3DZk5M7OPi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Authentication complete

public_tweets = api.search('muslims')


for tweet in public_tweets:
    analysis = TextBlob(tweet.text).correct()
    print(analysis.sentiment)
