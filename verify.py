from elasticsearch import Elasticsearch
import sys
es = Elasticsearch()
res = es.search(index="tweets", body={"query": {"match_all": {}}})
print("TOTAL: %d documents found \n" % res['hits']['total'])
print("\n10 Sample Document ID Stored in Elastic Search\n")
for doc in res['hits']['hits']:
        print (" Document ID: %s" % (doc['_id']))