from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from api.models import Mood
from api.serializers import MoodSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
from .contextIO import contextIOtest

class UserList(APIView):
    """
    List all users, or create a new user
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']

        user = User.objects.create_user(username, email, password, first_name = first_name, last_name = last_name) 

        if user is None:
            return Response({'error': 'Could not create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TokenList(APIView):
    """
    Create a new token
    """
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Bad username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({'error': 'User is inactive'}, status=status.HTTP_403_FORBIDDEN)

        token = Token.objects.get_or_create(user=user)
        return Response({ 'token': token[0].key })

class MoodList(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        user = request.user

        moods = user.mood_set.all()
        serializer = MoodSerializer(moods, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MoodSerializer(data=request.data)
    
        serializer.initial_data['user'] = request.user.id
        serializer.initial_data['time'] = datetime.now()
    
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        serializer.save()
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmailList(APIView):
    def get(self, request, format=None):
        emails = contextIOtest.main()
        return Response(emails)
