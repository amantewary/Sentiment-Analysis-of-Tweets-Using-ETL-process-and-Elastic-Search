# Sentiment Analysis of Tweets Using ETL process and Elastic Search

</br>


### Table of Contents


#### [1. Task Description](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#1-task-description-1)
#### [2. Twitter Tweet Extraction](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#2-twitter-tweet-extraction-1)
#### [3. Sentiment Analysis](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#3-sentiment-analysis-1)
#### [4. Loading Data into Elastic Search](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#4-loading-data-into-elastic-search-1)
#### [5. ETL as a batch process (BONUS)]()
#### [6. License](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#6-licence)

</br>

### 1. Task Description

Our task was to create an account on AWS(or any other cloud service provider) and twitter so that we could extract tweets and perform sentiment analysis on it. After that we load the result into ElasticSearch on Microsoft Azure Cloud. This assignment gives us an idea of how ETL works. 

We extracted more than 100 tweets after creating a twitter account and used the credentials to authenticate ourselves.

Sentiment Analysis of Tweets Using ETL processes and Elastic Search

</br>

### 2. Twitter Tweet Extraction

We are using **[tweepy](https://github.com/tweepy/tweepy)** to run a query and extract tweet into csv. Further, we cleaned the tweets and again created a new csv with nothing but pure texts. To clean the tweets we are making use of various regex and also we are encoding the tweets to "utf-8" because users were adding different emojis in their tweets.

![ScreenShot of tweet cleaning](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%2012.00.50%20PM.png?alt=media&token=c794e58f-1a17-4417-be76-5c01d4c99e35)

We are removing the following things from the tweets:
* URLs
* RTs and @
* Different language scripts


</br>


![ScreenShot of raw tweet](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%201.30.26%20PM.png?alt=media&token=0b287ed0-e495-461a-8200-fe8277b9e6a4)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Raw tweets before cleaning**


</br>


![ScreenShot of tweets after cleaning](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%201.30.41%20PM.png?alt=media&token=b65d7962-7345-48a6-ae23-8f8e440ead52)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Tweets after cleaning**


</br>

### 3. Sentiment Analysis

For performing sentiment analysis we are using the csv file that has clean tweets. A python library named **[vaderSentiment](https://github.com/cjhutto/vaderSentiment/tree/master/vaderSentiment)** was chosen to carry out sentiment analysis. Vader takes the entire sentence as input and spits out the polarity scores after analyzing the sentence. VaderSentiment uses something called "boosters" which gives additional scores to adjectives.

After performing the sentiment analysis, we are storing the output in a file "sentiment_output.csv" which has three columns, "Positive", "Negative" and "Neutral", respectively. These three columns gives the score of how much postive, negative or neutral the tweet was.

![Sentiment Analysis](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%201.30.57%20PM.png?alt=media&token=c551c79a-bce2-4a5f-bdfb-2e08251d20da)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Screenshot of Sentiment Analysis**



</br>

### 6. Licence

* The license of vaderSentiment

</br> 


>The MIT License (MIT)

>Copyright (c) 2016 C.J. Hutto

>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."