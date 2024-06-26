from bson import ObjectId
from utils.mongodb.MongoCollection import MongoCollection
from jsonschema import validate
from djangoapp.model import schema

class DjangoAppPersistence(MongoCollection):
    def __init__(self):
        super().__init__(collectionName='first')


    def create(self, newDocData):
        validate(instance=newDocData, schema=schema)
        return super().create(newDocData)

    def findById(self, id):
        result = super().findById(id)
        return self.mapResponse(result)
    
    def findByName(self, name):
        result = super().findByField('name', name)
        returnArr = []
        for doc in result: 
            returnArr.append(self.mapResponse(doc))
        return returnArr

    def mapResponse(self, doc): 
        return {
            'name': doc['name'],
            'isHeAGreatEngineer': doc['middle'],
            'userId': str(doc['_id'])
        }