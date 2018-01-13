'''
File Name: twitter_key_example.py
Author: Morgan Visnesky
Date: 01/12/2018

Description:

Example of a way to keep your twitter, and other api keys in a seperate .py file
and import into your application as is done in the tweet_sentiment.py file.
Some documentation to help you better understand this can be found here:
http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html

Despite this not being the best practice available, it does make the key code easily seperatable
from the main appication file for purposes of sharing the code and NOT your private keys.
There are many articles and resources available to help you better understand other methods of
doing this such as storing your keys in environment variables.
'''

# First import tweepy
import tweepy

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')

# Follow the auth_tutorial link above to see the procedure for generating a request token
# which you will need to do to proceed
token = auth.set_access_token('key', 'secret') 
