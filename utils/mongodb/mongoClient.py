import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1/pymongo')
db = client['pymongo']