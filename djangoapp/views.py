from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view

from djangoapp.FirstService import FirstService
from djangoapp.persistence import DjangoAppPersistence

@api_view(['POST', 'GET'])
def index(request):
    newUserData = JSONParser().parse(request)
    result = FirstService().create_pymongoObject(newUserData=newUserData)
    return JsonResponse(data=result,status=status.HTTP_201_CREATED)

def findByName(request, name):
    result = FirstService().findByName(name)
    return JsonResponse(data=result,status=status.HTTP_200_OK)
