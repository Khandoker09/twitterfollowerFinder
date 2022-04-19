'''
This script was written to generate the list of follower form a single account 
it will provide a .csv file with name and other detail of the followers 
Author: Khandoekr Tanjim Ahammad
Date: 2022.04.19
Comments: 
'''
#Import libraries 
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time
import datetime
# for creating the file name
current_date = datetime.datetime.now()
#all the api keys from the developer accounts 
consumer_key = "key"
consumer_secret = "key"
access_key = "key"
access_secret = "key"
# Pass your twitter credentials to tweepy via its OAuthHandler
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)
# Creation of query for finding the followers . parameter = screen_nmae
followers = tweepy.Cursor(api.get_followers, screen_name="airtablestatus").items()  

# Pulling information from tweets iterable object
try:
# Add or remove tweet information you want in the below list comprehension
    followers_list = [[tweet.name,tweet.screen_name, tweet.id_str,tweet.location, tweet.url, tweet.description, tweet.verified, tweet.followers_count, tweet.friends_count, tweet.statuses_count, tweet.listed_count, tweet.created_at, tweet.profile_image_url_https, tweet.default_profile] for tweet in followers]
# Creation of dataframe from tweets_list
except:
    followers_list = [[tweet.name,tweet.screen_name, tweet.id_str,tweet.location, tweet.url, tweet.description, tweet.verified, tweet.followers_count, tweet.friends_count, tweet.statuses_count, tweet.listed_count, tweet.created_at, tweet.profile_image_url_https, tweet.default_profile] for tweet in followers]
    time.sleep(15)
# Did not include column names to simplify code 
followers_list_df = pd.DataFrame(followers_list)
followers_list_df.columns = ['username','user_screenname','userid','userslocation','usersurl','usersdescription','userverified','followerscount','friendscount','statusescount','listedcount','createdat','profileimageurlhttps','defaultrofile']

filename = str('twitter_followers_list_')+str(current_date.year)+str('_')+str(current_date.month)+str('_')+str(current_date.day)
print(followers_list_df)
followers_list_df.to_csv(str(filename + '.csv'),index=False)
