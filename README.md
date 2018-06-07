# Sentiment Analysis of Tweets Using ETL process and Elastic Search

</br>


### Table of Contents


#### [1. Task Description](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#1-task-description-1)

#### [2. Installation Notes](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#2-twitter-tweet-extraction-1)
#### [3. Twitter Tweet Extraction](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#2-twitter-tweet-extraction-1)
#### [4. Sentiment Analysis](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#3-sentiment-analysis-1)
#### [5. Loading Data into Elastic Search](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#4-loading-data-into-elasticsearch)
#### [6. ETL as a batch process (BONUS)](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#5-etl-as-a-batch-process-bonus-1)
#### [7. License](https://github.com/amantewary/Sentiment-Analysis-of-Tweets-Using-ETL-process-and-Elastic-Search#6-licence)

</br>

### 1. Task Description

Sentiment Analysis of Tweets Using ETL processes and Elastic Search was the objective of this Assigment. We were instructed to create an account on AWS(or any other cloud service provider) and twitter so that we could extract tweets and perform sentiment analysis on it. We are using python 3 for this Assignment. After that we load the result into ElasticSearch on Microsoft Azure Cloud. This assignment gives us an idea of how ETL works. 

We extracted more than 100 tweets after creating a twitter account and used the credentials to authenticate ourselves.


</br>


### 2. Installation Notes


To be able to run this program, you need to have the following things:

* python 3 (if not present)
* pip3 (if not present)
* pandas
* tweepy
* VaderSentiment library
* elasticSearch
* ElasticSearch DSL
* more_etertools library

#### Build Instructions:

1. To install python3 execute this command.

        sudo apt-get install -y python3-pip
        
2. Using pip you have to intall other libraries. To install tweepy execute this command.

        pip3 install tweepy
        
3. Install pandas next by executing this command.

        sudo -H pip3 install pandas
        
4. Install the vaderSentiment which is required for performing sentiment analysis.

        pip3 install vaderSentiment
        
5. Lastly, install more_itertools by executing this command.

        pip3 install more-itertools
 
6. Now, to be able load the data into elasticsearch, we need to install libararies that enables us to do that. Execute the following command to install elasticsearch.

        wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

        sudo apt-get install apt-transport-https

        echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

        sudo apt-get update && sudo apt-get install elasticsearch

7.  To run this program from a bash shell you'll have to write the following command.

        ./tweet



</br>

### 3. Twitter Tweet Extraction

We are using **[tweepy](https://github.com/tweepy/tweepy)** to run a query and extract tweet into csv. Further, we cleaned the tweets and again created a new csv with nothing but pure texts. To clean the tweets we are making use of various regex and also we are encoding the tweets to "utf-8" because users were adding different emojis in their tweets.

We ran our query to find tweets from the following hashtags and usernames:

* #HanSolo
* Nova Scotia
* @Windows
* #realDonaldTrump
* #iOS12
* #Mojave
* #E3
* #Pokemon


Following is the code by which we are cleaning the tweets.

![ScreenShot of tweet cleaning](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%2012.00.50%20PM.png?alt=media&token=c794e58f-1a17-4417-be76-5c01d4c99e35)

We are removing the following things from the tweets:
* URLs
* RTs and @
* Different language scripts



We are also adding multiple filters like **language filter** and retweet filter to retrieve tweets in english and remove redundant tweets.

</br>


![ScreenShot of raw tweet](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%201.30.26%20PM.png?alt=media&token=0b287ed0-e495-461a-8200-fe8277b9e6a4)

**Raw tweets before cleaning**


</br>


![ScreenShot of tweets after cleaning](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%201.30.41%20PM.png?alt=media&token=b65d7962-7345-48a6-ae23-8f8e440ead52)

**Tweets after cleaning**


</br>

### 4. Sentiment Analysis

For performing sentiment analysis we are using the csv file that has clean tweets. A python library named **[vaderSentiment](https://github.com/cjhutto/vaderSentiment/tree/master/vaderSentiment)** was chosen to carry out sentiment analysis. Vader takes the entire sentence as input and spits out the polarity scores after analyzing the sentence. VaderSentiment uses something called "boosters" which gives additional scores to adjectives.


![Snap of boosters in Vader](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%203.14.55%20PM.png?alt=media&token=5c8673bb-8ace-4b39-87a0-f84b241a0219)

**Snap of booster in vaderSentiment Library**


After performing the sentiment analysis, we are storing the output in a file "sentiment_output.csv" which has three columns, "Positive", "Negative" and "Neutral", respectively. These three columns gives the score of how much positive, negative or neutral the tweet was.

![Sentiment Analysis](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-06%20at%2011.53.15%20PM.png?alt=media&token=5cfaa3a2-726d-474d-90ef-7f8b8950e447)


**Screenshot of Sentiment Analysis**

</br>

### 5. Loading Data Into Elasticsearch

After the sentiment analysis is completed, we are loading the output data stored in “sentiment_output.csv” to Elasticsearch using Elasticsearch bulk helper function. The bulk function takes the instance of Elasticsearch and DictReader, index name (“tweets”)and document type(“sentiments”). In case the index already exists, it will delete the index and then will load the data.


![Loading data into ElasticSearch](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-07%20at%201.49.27%20PM.png?alt=media&token=53328320-5b63-47b1-a441-6b353742cd61)

**Loading data into ElasticSearch**

</br>


### 6. ETL as a batch process (BONUS)

To run all three processes of extracting data from twitter, performing sentiment analysis and loading output in Elastic Search, a shell script using Linux Shell commands is created (./tweet). It will be used to run all the three process in a single batch job with no user intervention required and that runs as a background process.


![Shell script](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Screen%20Shot%202018-06-07%20at%206.44.10%20PM.png?alt=media&token=ba224d98-7d42-4f0d-97c7-7c6ff9187eb7)

**Shell Script**


#### Output

![Expected Output](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/WhatsApp%20Image%202018-06-07%20at%207.06.45%20PM.jpeg?alt=media&token=0bbe9652-172c-46c3-a972-6a7a73aa66f0)

</br>

### 7. Licence

* The license of vaderSentiment

</br> 


>The MIT License (MIT)
>
>Copyright (c) 2016 C.J. Hutto
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."