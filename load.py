import csv

from elasticsearch import helpers, Elasticsearch
from elasticsearch_dsl import connections
connections.create_connection(hosts=['localhost'],timeout=20)


es = Elasticsearch()

with open('sentiment_output.csv') as f:
        reader = csv.DictReader(f)
        if es.indices.exists('tweets'):
                es.indices.delete(index='tweets', ignore=[400, 404])
                helpers.bulk(es,reader, index = 'tweets', doc_type = 'sentiments')
        else:
                helpers.bulk(es,reader, index='tweets', doc_type = 'sentiments')