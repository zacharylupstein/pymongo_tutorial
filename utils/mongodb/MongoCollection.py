from bson import ObjectId
from utils.mongodb.mongoClient import db

class MongoCollection: 
    def __init__(self, collectionName):
        self.collectionName = collectionName
        self.collection = db[self.collectionName]

    def create(self, params):
        return self.collection.insert_one(params).inserted_id

    def findById(self, id):
        foundDoc = self.collection.find_one({"_id": ObjectId(id)})
        return foundDoc
    
    def findByField(self, field, searchValue):
        foundDocs = self.collection.find({field: searchValue})
        return foundDocs

