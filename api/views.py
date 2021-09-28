from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import UserProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .serializers import User_profileSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
@api_view(['GET'])
def user_exist_actknowlage(request):
    email=request.data['email']
    actknwolage=UserProfile.objects.filter(email=email).exists()
    print(actknwolage)
    return Response(data=actknwolage, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    email=request.data['email']
    user_name=request.data['user_name']
    password=request.data['password']
    phone=request.data['phone']
    name=request.data['name']
    last_name=request.data['last_name']
    if not User.objects.filter(username=user_name).exists():
        user=User.objects.create_user(username=user_name,password=password)
        user_profile=UserProfile.objects.create(user_name=user,phone=phone,name=name,last_name=last_name,
                                                email=email)
        return Response(data='success', status=status.HTTP_200_OK)
    else:
        return Response(data='user_name is already taken' ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_login(request):
    user_name=request.data['user_name']
    password = request.data['password']
    user=authenticate(username=user_name, password=password)
    if user :
        return Response(data='successfully logged in', status=status.HTTP_200_OK)
    else:
        return Response(data='username or password invalid', status=status.HTTP_401_UNAUTHORIZED)
