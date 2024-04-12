from users.userPersistence import UserPersistence

def createUser(newUserData):
    userPersistence = UserPersistence()
    usersWithEmail = userPersistence.findByEmail(email=newUserData['email'])

    if len(usersWithEmail) > 0: 
        print(usersWithEmail)
    
    newUserId = userPersistence.create(newUserData=newUserData)
    foundUser = userPersistence.findById(id=newUserId)
    return foundUser

def updateUser(id, updateData):
    userPersistence = UserPersistence()
    userPersistence.updateUser(id, updateData=updateData)

    return userPersistence.findById(id)

def getUserById(id):
    userPersistence = UserPersistence()
    return userPersistence.findById(id)