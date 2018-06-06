# Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search


### Table of Contents


#### [1. Task Description]()
#### [2. Twitter Tweet Extraction]()
#### [3. Sentiment Analysis]()
#### [4. Loading Data into Elastic Search]()
#### [5. ETL as a batch process]()

</br>

### 1. Task Description

Our task was to create an account on AWS(or any other cloud service provider) and twitter so that we could extract tweets and perform sentiment analysis on it. After that we load the result into ElasticSearch on Microsoft Azure Cloud. This assignment gives us an idea of how ETL works. 

We extracted more than 100 tweets after creating a twitter account and used the credentials to authenticate ourselves.

Sentiment Analysis of Tweets Using ETL process and Elastic Search

</br>

### 2. Twitter Tweet Extraction

We are using [tweepy](https://github.com/tweepy/tweepy) to run a query and extract tweet into csv. Further, we cleaned the tweets and again created a new csv with nothing but pure texts. To clean the tweets we are making use of various regex and also we are encoding the tweets to because users were adding different emojis in their tweets.

