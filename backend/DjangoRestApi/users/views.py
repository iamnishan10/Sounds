from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer
...
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        tutorials = User.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            users = users.filter(title__icontains=title)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            user = users.filter(title__icontains=title)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    try: 
        user = User.objects.all()
    except: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


