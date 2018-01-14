#!/usr/bin/env python
"""
Application to use sentiment analysis on user determined tweets then store
resulting data in SQLite database.


tweet_sentiment.py uses python in conjunction with the tweepy, and TextBlob
packages for crawling tweets and perfroming sentiment analysis respectively.
After inputing a comma seperated list of user defined keywords, and then
entering a valid twitter handle tweet_sentiment.py will grab valid tweets
correlating to the user defined keywords from the 100 most recent tweets of the
selcted twitter handle.

Minimal functionality is currently implemented to parse for links and future
plans exist to have it follow those links and parse them as well, returning
additional sentiment data, to possibly be averaged into the original sentiment
in a meaningful way.

All data returned from the search is stored in a SQLite database, the name of
which is printed to the screen upon completion of the search along with the
number of relevant tweets stored in the database.

TODO:
    ** add contextual semantic search
    ** add intent analysis

    - tweet_cleaner() function, see example below
    (in_progress)- ext_link_parser() function to follow link, parse webpage
    - save date to db with tweet (use tweet_created_at method with tweepy for tweet date and time)
    * also store the current date of datetime of the tweet grab
    - break __main__ up into smaller reusable functions

    - make it so it you dont want to enter any keywords and just return all tweets from a given user you can
      just grab thier last 100 tweets by default.
    - display last used search terms in form of list (terms from last search session), allow selection of that
      as opposed to entering in new list of terms or defaulting to no search terms.

This file is part of python_twitter_sentiment.

python_twitter_sentiment is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
python_twitter_sentiment is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Morgan Visnesky"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "morganticss@gmail.com"
__date__ = "2018/01/02"
__license__ = "GPLv3"
__maintainer__ = "Morgan Visnesky"
__status__ = "Developement"
__version__ = "0.0.1"


import datetime
import re
import sqlite3
import tweepy
import json
from textblob import TextBlob as tb
#import urllib.request
#from bs4 import BeautifulSoup
from morgstwtkey import auth, token
auth #OAuth
token #Access token
api = tweepy.API(auth)

#create a tweet cleaning function to pass tweets through before the get_sentiment function
'''
TODO:
def tweet_cleaner(tweet):
    - make sure textblob removes stopwords, if not do so.
    - clean punctuation
    - separate links from tweets if links exist
    - return cleaned tweet, and list of weblinks
'''

'''
TODO:
def ext_link_parser(link):
    - go to link and parse (maybe use beautifulSoup)
    - return sentiment to a large body of text anywhere in the link that key
      words from the user are found
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
                                                                link_in_tweet text)''')

    keywords = get_user_keywords()

    twitter_name = input("Enter a Twitter Handle: ")
    for name in twitter_name:
        try:
            stuff = api.user_timeline(screen_name = twitter_name,
                                    count = 100,
                                    include_rts = False,
                                    tweet_mode= 'extended')
            # tweet_mode = 'extended'  in addition status.full_text accurately grabs
            # entire tweet with t.co link at end

        except tweepy.TweepError as e:
            twitter_name = input("The handle you entered was invalid, please try again: ")
        catchcount = 0 # used to keep track of num of tweets returned

    for status in stuff:
        for word in keywords:
            if word in status.full_text.lower(): # lowercase as cleaning measure for proper matching

                # re.search + link grabber
                url = ''
                links = re.search("(?P<url>https?://[^\s]+)", status.full_text)
                if links:
                    url = links.groups()
                    url = url[0]
                # status passed to sentiment function
                sent = get_sentiment(status.full_text.lower())
                # data inserted in to corresponding DB columns
                cur.execute("INSERT INTO twitter_sentiment VALUES (?,?,?,?,?)", (twitter_name, status.full_text, word, sent, str(url)))
                catchcount += 1 # if keyword is in tweet and has been collected add 1 to catchcount

            else:
                continue

    '''
    TODO: Return the number of links stored from current search with list of attached links
    '''
    print('\nThis search caught %d tweets' % catchcount)
    print('Data was added to: %s \n' % filename)

    conn.commit()
    conn.close()
__main__()
