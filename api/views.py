from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import UserProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .serializers import User_profileSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@api_view(['GET'])
def user_exist_actknowlage(request):
    email=request.data['email']
    device = request.data.get('device')
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
    device = request.data.get('device')
    if not User.objects.filter(username=user_name).exists():
        user=User.objects.create_user(username=user_name,password=password)
        UserProfile.objects.create(user_name=user,phone=phone,name=name,last_name=last_name,
                                                email=email)
        return Response(data='success', status=status.HTTP_200_OK)
    else:
        return Response(data='user_name is already taken' ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_login(request):
    user_name=request.data['username']
    password = request.data['password']
    device = request.data.get('device')
    user=authenticate(username=user_name, password=password)
    if user :
        token , created =Token.objects.get_or_create(user=user)
        return Response(data={'token' : token.key}, status=status.HTTP_200_OK)
    else:
        return Response(data='username or password invalid', status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    content='Token is working'
    return Response(content)