import tweepy
import time
import json
import csv
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
connections.create_connection(hosts=['localhost'],timeout=20)

consumer_key = "DSaMQVLUbCMCNACL9cNGPBFhL"
consumer_secret = "NKdMDnPfdxO99G0smWtA8GHBrAJHnP6DVoikP0UFyiloSKkgEP"
access_key = "1000039197753868291-TGOXH3jWGfOK9g5oWznKWbF5D1NYQd"
access_secret = "T1nOwu1yc0RMcFMZjFkpNJCnUlU4KTr2zPuyK4GRjtxTg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_profile(screen_name):
        api = tweepy.API(auth)
        try:
                user_profile = api.get_user(screen_name)
                print(screen_name)
        except tweepy.error.TweepError as e:
                user_profile = json.loads(e.response.text)
        return user_profile
def get_trends(location_id):
        api = tweepy.API(auth)
        try:
                trends = api.trends_place(location_id)
        except tweepy.error.TweepError as e:
                trends = json.loads(e.response.text)
        return trends
def get_tweets(query):
        api=tweepy.API(auth)
        try:
                tweets = api.search(query)
        except tweepy.error.TweepError as e:
                tweets = [json.loads(e.response.text)]
        return tweets
tw = get_tweets("#HanSolo")

queries = ["#HanSolo", "\"Nova Scotia\"","@Windows", "#realDonaldTrump"]

with open ('tweet.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['id', 'user', 'created_at', 'text'])
        for query in queries:
                t= get_tweets(query)
                for tweet in t:
                        print (tweet.user.screen_name)
                        writer.writerow([tweet.id_str, tweet.user.screen_name, tweet.created_at, tweet.text])