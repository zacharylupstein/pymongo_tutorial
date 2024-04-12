from bson import ObjectId
from utils.mongodb.MongoCollection import MongoCollection
from jsonschema import validate
from users.model import schema, updateSchema

class UserPersistence(MongoCollection):
    def __init__(self):
        super().__init__(collectionName='users')

    def create(self, newUserData):
        validate(instance=newUserData, schema=schema)
        return super().create(newUserData)

    def findById(self, id):
        result = super().findById(id)
        return self.mapResponse(result)
    
    def findByEmail(self, email):
        result = super().findByField('email', email)
        returnArr = []
        for doc in result: 
            returnArr.append(self.mapResponse(doc))
        return returnArr
    
    def updateUser(self, id, updateData):
        validate(instance=updateData, schema=updateSchema)
        return super().updateOne(id=id, updateData=updateData)


    def mapResponse(self, doc): 
        doc['userId'] = str(doc['_id'])
        del doc['_id']
        return doc