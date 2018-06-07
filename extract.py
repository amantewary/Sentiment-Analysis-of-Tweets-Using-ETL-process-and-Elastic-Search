import tweepy
import json
import csv

consumer_key = "DSaMQVLUbCMCNACL9cNGPBFhL"
consumer_secret = "NKdMDnPfdxO99G0smWtA8GHBrAJHnP6DVoikP0UFyiloSKkgEP"
access_key = "1000039197753868291-TGOXH3jWGfOK9g5oWznKWbF5D1NYQd"
access_secret = "T1nOwu1yc0RMcFMZjFkpNJCnUlU4KTr2zPuyK4GRjtxTg"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]
    return tweets

queries = ["#HanSolo -filter:retweets lang:en", "\"Nova Scotia\" -filter:retweets lang:en",
           "@Windows -filter:retweets lang:en", "#realDonaldTrump -filter:retweets lang:en",
           "#iOS12 -filter:retweets lang:en", "#Mojave -filter:retweets lang:en", "#E3 -filter:retweets lang:en", "#Pokemon -filter:retweets lang:en"]

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
