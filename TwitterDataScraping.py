import tweepy
import pandas as pd

#asking user for a keyword or a hashtag to make a specfied query
keyword=input("Enter a keyword/hashtag")
# =============================================================================
# file=input("Enter the name of the file you want to save the retrieved data in:")
# =============================================================================
#account credentials

api_key="lbWttBAnADT0gLx4mVTtl5Hl9"
api_key_secret="PZbSRvAHdwho34s2vh0eIEDxsC211DizCrtdG99ChhCQ91IHIE"
access_token="1500902573838323713-FyIlCN3pLdqHhjwIqvcRlYCJzq4DiP"
access_token_secret="rrkLhDagm1fJT8SH045VApIblocofbfQCbjn6alRHfMTm"

#authentication
auth=tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#api instance will give you access to your twitter account and then you can tweet or delete tweet etc
#I will use it to get the public tweets. It is mainly used to use methods to manipulate/fetch tweets.
#cursor method will return as many tweets as requested, whereas the timeline() method will return atmost 200 tweets per reqyes
#count parameter is added to retrieve the number of results per page 
limit=400#Need just 10 tweets per query.

#if the tweet_mode is not set to extended, it'll fetch only 140 char from each tweet by default.
new_search=keyword+"-filter:retweets"
data = tweepy.Cursor(api.search_tweets, q=new_search, lang="eng", tweet_mode='extended', count=500).items(limit)
field_names=['time', 'user', 'tweet_texts']
info=[]
for item in data:
    
    info.append([item.created_at, item.user.screen_name, item.full_text])
#creating a dataframe here.
table=pd.DataFrame(info, columns=field_names)
#transferring the data in the dataframe to a .csv file.
print(table)
table.to_csv("file.csv", mode='a')