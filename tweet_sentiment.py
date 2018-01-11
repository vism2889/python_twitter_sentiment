'''
File Name: tweet_sentiment.py
Author: Morgan Visnesky
Date: 01/02/2018

Description:

Application to use sentiment analysis on user determined tweets then store resulting
data in SQLite database.

Planned Improvements:

    - tweet_cleaner() function, see example below
    - ext_link_parser() function to follow link, parse webpage
        - find way to save/ compress parsed data as accessible file format
        -
    - save date to db with tweet
    - break __main__ up into smaller reusable functions

'''
import re
import sqlite3
import tweepy
import json
#import sentiment
from textblob import TextBlob as tb


# make demo file showing how to store auth, and token in seperate file
from morgstwtkey import auth, token
auth #OAuth
token #Access token
api = tweepy.API(auth)




#create a tweet cleaning function to pass tweets through before the get_sentiment function
'''
def tweet_cleaner(tweet):
    - make sure textblob removes stopwords, if not do so.
    - clean punctuation
    - separate links from tweets if links exist
    - return cleaned tweet, and list of weblinks
'''

'''
def ext_link_parser(link):
    - go to link and parse (maybe use beautifulSoup)
    - return sentiment to a large body of text anywhere in the link that key words from the user are found
    -

'''

def get_sentiment(tweet):
    sent_analysis = tb(tweet)
    SA = sent_analysis.sentiment.polarity
    if SA > 0:
        return 'positive'
    elif SA == 0:
        return 'neutral'
    else:
        return 'negative'

def get_user_keywords():
    user_words = ()
    keywords = input('Enter keywords as a comma separted list: \n')
    kw = tb(keywords)
    return kw.words.lower()

def __main__():
    filename = 'twitter_sentiment_test.db'
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS twitter_sentiment(twitter_handle text, tweet text, keyword text, sentiment text)')

    keywords = get_user_keywords()

    twitter_name = input("Enter a Twitter Handle: ")
    for name in twitter_name:
        try:
            stuff = api.user_timeline(screen_name = twitter_name, count = 100, include_rts = False)
        except tweepy.TweepError as e:
            twitter_name = input("The handle you entered was invalid, please try again: ")
        catchcount = 0
    for status in stuff:
        for word in keywords:
            if word in status.text.lower():
                sent = get_sentiment(status.text)
                cur.execute("INSERT INTO twitter_sentiment VALUES (?,?,?,?)", (twitter_name, status.text, word, sent))
                catchcount += 1
            else:
                continue

    print('\nThis search caught %d tweets' % catchcount)
    print('Data was added to: %s \n' % filename)

    conn.commit()
    conn.close()
__main__()
