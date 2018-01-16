# python_twitter_sentiment

First 'working' sentiment grabber I've made with python.  (I know... like you haven't seen one of these already...)

Hoping to go all out with this in my free time over the next couple of months,
currently basing the functionality around "grabbing" data but also aim to 
come up with interesting ways to "respond" and interact with the data.

Requirements:
- Python 3.5 or newer.
- Active twitter account with API key.
- [Tweepy](https://github.com/tweepy/tweepy)
- [TextBlob](https://github.com/sloria/textblob)
**** 
- The program grabs tweets from a specific twitter handle based on user
  determined keywords.
- Resulting data from the tweet grab gets run through a basic tokenization
  and sentiment grabbing function using the TextBlob package.
- Data is then stored in a SQLite DB.

****

Future Improvements:
- Clean tweets better.
- Follow links inside of tweets to parse and perfrom sentiment analysis on.
- Implement more search options ex:(search by location, hashtag,...).
- Add a few numerical analysis functions to return statistical data to 
  the user.
- Add function to store other words in the tweet that werent the selected
  keywords, for future comparisons/analysis.
- Add compare functions:
	- Compare by twitter handles
	- Compare by keyword
	
Further Reading and Resources: (Some of these are for NLTK package,
which isn't currently being used as of late.)
- [noun-phrase extractor code](https://gist.github.com/shlomibabluki/5539628)
- [noun-phrase extractor article](https://thetokenizer.com/2013/05/09/efficient-way-to-extract-the-main-topics-of-a-sentence/)
- [twitter sentiment-analysis article series](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-5-50b4e87d9bdd)
- [intent/contextual semantic search article](https://towardsdatascience.com/sentiment-analysis-concept-analysis-and-applications-6c94d6f58c17)

