'''
File Name: tweet_sentiment.py
Author: Morgan Visnesky
Date: 01/02/2018

Description:

Application to use sentiment analysis on user determined tweets then store resulting
data in SQLite database.

Planned Improvements:

    - tweet_cleaner() function, see example below
    (in_progress)- ext_link_parser() function to follow link, parse webpage
    - save date to db with tweet (use tweet_created_at method with tweepy for tweet date and time)
    * also store the current date of datetime of the tweet grab
    - break __main__ up into smaller reusable functions

    - make it so it you dont want to enter any keywords and just return all tweets from a given user you can


'''
import datetime
import re
import sqlite3
import tweepy
import json
#import sentiment
from textblob import TextBlob as tb
#import urllib.request
#from bs4 import BeautifulSoup


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
    sent_analysis = tb(tweet) # creates textBlob object which tokenizes the tweet
    SA = sent_analysis.sentiment.polarity # returns a value between -1 and 1
    if SA > 0:
        return 'positive'
    elif SA == 0:
        return 'neutral'
    else:
        return 'negative'

def get_user_keywords():
    user_words = ()
    keywords = input('Enter keywords as a comma separted list: \n')
    kw = tb(keywords) #creates a textBlob object of user inputted comma-seperated list of keywords
    return kw.words.lower() # lowercase as a cleaning measure

def __main__():
    filename = 'twitter_sentiment_test.db'
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS twitter_sentiment(twitter_handle text,
                                                                tweet text,
                                                                keyword text,
                                                                sentiment text,
                                                                link(s)_in_tweet text)''')

    keywords = get_user_keywords()

    twitter_name = input("Enter a Twitter Handle: ")
    for name in twitter_name:
        try:
            stuff = api.user_timeline(screen_name = twitter_name, count = 100, include_rts = False)
            # api.user_timeline currently doesnt return full tweet, returns partial with t.co link at the end
            # created link grabber, but it seems the t.co links are unreasonably hard to parse for one
            # tweets worth of data.
        except tweepy.TweepError as e:
            twitter_name = input("The handle you entered was invalid, please try again: ")
        catchcount = 0

    for status in stuff:
        for word in keywords:
            if word in status.text.lower(): # lowercase as cleaning measure for proper matching

                # re.search + link grabber
                # would eventually like to create another one specific for external weblinks
                # and use this one for t.co links specifically unless can manage another way to return full tweets
                # from tweepy
                url = ''
                links = re.search("(?P<url>https?://[^\s]+)", status.text)
                if links:
                    url = links.groups()
                    url = url[0]



                sent = get_sentiment(status.text)
                cur.execute("INSERT INTO twitter_sentiment VALUES (?,?,?,?,?)", (twitter_name, status.text, word, sent, str(url)))
                catchcount += 1

            else:
                continue

    print('\nThis search caught %d tweets' % catchcount)
    print('Data was added to: %s \n' % filename)

    conn.commit()
    conn.close()
__main__()
