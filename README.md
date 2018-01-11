# python_twitter_sentiment

First 'working' sentiment grabber I've made with python.  (I know... like you haven't seen one of these already...)

Hoping to go all out with this in my free time over the next couple of months,
currently basing the functionality around "grabbing" data but also aim to 
come up with interesting ways to "respond" and interact with the data.

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
	
