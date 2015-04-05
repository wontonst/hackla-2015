from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from api.models import Mood
from api.serializers import MoodSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

@api_view(['GET', 'POST'])
def users(request):
    """
    List all users, or create a new user
    """
    if request.method == 'GET':
        return get_users(request)
    elif request.method == 'POST':
        return post_users(request)

def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def post_users(request):
    email = request.data['email']
    username = request.data['username']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']

    user = User.objects.create_user(username, email, password, first_name = first_name, last_name = last_name) 

    if user is None:
        return Response({'error': 'Could not create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def tokens(request):
    if request.method == 'POST':
        return post_tokens(request)

def post_tokens(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Bad username or password'}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.is_active:
        return Response({'error': 'User is inactive'}, status=status.HTTP_403_FORBIDDEN)

    token = Token.objects.get_or_create(user=user)
    return Response({ 'token': token[0].key })

def moods(request):
    if request.method == 'GET':
        return get_moods(request)
    elif request.method == 'POST':
        return post_moods(request)

def get_moods(request):
    user = request.user

    moods = Mood.objects.filter(user__exact=user)
    serializer = MoodSerializer(moods, many=True)
    return Response(serializer.data)

def post_moods(request):
    serializer = MoodSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

