from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view

from users.service import createUser, updateUser, getUserById

@api_view(['POST'])
def user(request):
    newUserData = JSONParser().parse(request)
    result = createUser(newUserData=newUserData)
    return JsonResponse(data=result,status=status.HTTP_201_CREATED)

@api_view(['PATCH', 'GET'])
def userDetail(request, id):
    print("its in here")
    if request.method == "PATCH":
        updateData = JSONParser().parse(request)
        result = updateUser(id, updateData=updateData)
        return JsonResponse(data=result,status=status.HTTP_200_OK)
    if request.method == "GET":
        print("its in here")
        result = getUserById(id)
        return JsonResponse(data=result,status=status.HTTP_200_OK)
    
