from djangoapp.persistence import DjangoAppPersistence

class FirstService: 
    def create_pymongoObject(self, newUserData):
        firstPersistence = DjangoAppPersistence()
        newUserId = firstPersistence.create(newUserData)
        foundUser = firstPersistence.findById(newUserId)
        return foundUser
    
    def findByName(self, name):
        docs = DjangoAppPersistence().findByName(name=name)
        return {
            'items': docs, 
            'page': 1, 
            'perPage': 10, 
            'total': len(docs)
        }