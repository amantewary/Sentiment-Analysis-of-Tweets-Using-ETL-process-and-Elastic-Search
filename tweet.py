import tweepy
import time
import json
import operator
import csv
import pandas as pd

import re
from more_itertools import unique_everseen

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# from elasticsearch import Elasticsearch
# from elasticsearch_dsl import connections
# connections.create_connection(hosts=['localhost'],timeout=20)

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
    api = tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]
    return tweets


# tw = get_tweets("#HanSolo")


queries = ["#HanSolo -filter:retweets lang:en", "\"Nova Scotia\" -filter:retweets lang:en",
           "@Windows -filter:retweets lang:en", "#realDonaldTrump -filter:retweets lang:en",
           "#iOS12 -filter:retweets lang:en", "#Mojave -filter:retweets lang:en", "#E3 -filter:retweets lang:en"]


with open('tweet.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id', 'user', 'created_at', 'text'])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            writer.writerow([(tweet.id_str),
                             (tweet.user.screen_name),
                             tweet.created_at,
                             (tweet.text.encode("utf-8"))])
#
# '''
# Code to clean the tweets for analysis
# '''
#
# df = pd.read_csv('tweet.csv')
#
# df_clean = df.drop_duplicates(subset=['text'])
#
# df_clean.to_csv('tweet.csv')
# df.update(df_clean)
# lists = []
# for index, row in df_clean.iterrows():
#     '''Code to remove Url, RTs and # tags were inspired from:
#     1. https://stackoverflow.com/a/8377440/3966666
#     2. https://knowledge.safe.com/questions/29604/regex-to-extract-url-from-tweet.html
#     '''
#
#     text = row['text']
#     text = re.sub("http[a-zA-Z]?:\/\/?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?", '',text).strip()
#     text = re.sub('RT @[\w_]+:', '', text)
#     text = re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"', '', text)
#     lists.append(text)
#
#
# print(lists)
#
# for index, row in df_clean.iterrows():
#
#     row['text'] = lists[index]
#
#
# df.update(df_clean)
# df.to_csv('clean_tweet.csv')
lists = []
with open('clean_tweet.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['id', 'user', 'created_at', 'text'])
        i = 0
        for query in queries:
                t = get_tweets(query)
                for tweet in t:
                        ####
                        '''Code to remove Url, RTs and # tags were inspired from:
                        1. https://stackoverflow.com/a/8377440/3966666
                        2. https://knowledge.safe.com/questions/29604/regex-to-extract-url-from-tweet.html
                        '''
                        ####

                        text = re.sub(r"http[a-zA-Z]?:\/\/?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?", '',
                                      tweet.text).strip()
                        # text = re.sub('RT @[\w_]+:', '', text)
                        text = re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"', '', text)

                        lists.append(text)
                        list(unique_everseen(lists))
                        writer.writerow([(tweet.id_str),
                                         (tweet.user.screen_name),
                                         tweet.created_at,
                                         lists[i]])
                        i += 1



'''
Code to remove duplicates the tweets for analysis
'''

df = pd.read_csv('clean_tweet.csv')

df_clean = df.drop_duplicates(subset=['text'])
lists = df_clean['text'].tolist()
df_clean.to_csv('clean_tweet.csv', index=False)


analyzer = SentimentIntensityAnalyzer()


vs = {}
sentimentList = []
pos = []
neg = []
neu = []
for sentence in lists:
    vs = analyzer.polarity_scores(sentence)
    # print(" {:-<65} {} ".format(sentence, str(vs)))
    sentimentList.append(max(vs.items(), key=operator.itemgetter(1))[0])
    # print (max(vs.items(), key=operator.itemgetter(1))[0])
    pos.append(vs['pos'])
    neg.append(vs['neg'])
    neu.append(vs['neu'])








with open('sentiment_output.csv', 'w') as f2:
    with open('clean_tweet.csv', 'r') as infile:
        next(infile)
        reader = csv.reader(infile)
        writer = csv.writer(f2)
        writer.writerow(['id', 'user', 'created_at', 'text', 'pos', 'neg', 'neu'])

        i=0
        for rows in reader:
            rows.append(pos[i])
            rows.append(neg[i])
            rows.append(neu[i])
            writer.writerow(rows)
            i += 1






