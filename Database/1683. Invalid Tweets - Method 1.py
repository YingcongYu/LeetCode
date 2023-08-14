# Write a solution to find the IDs of the invalid tweets. 
# The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

# Return the result table in any order.


import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
