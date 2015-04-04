from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == 'GET':
        return render(request, 'website/signup.html', {})

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['passwd']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        user = User.objects.create_user(username, email, password, first_name = firstname, last_name = lastname) 

        return render(request, 'website/user-created.html', 
            { 'email': email, 
            'firstname': firstname, 
            'lastname': lastname })

def signin(request):
    if request.method == 'GET':
        return render(request, 'website/signin.html', {})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if '@' in username:
            user = authenticate(username=username, password=password)
        else:
            user = authenticate(username=username, password=password)

        if user is None:
            return render(request, 'website/invalid-login.html', {})
        else:
            if not user.is_active:
                return render(request, 'website/user-disabled.html', {})
            else:
                login(request, user)
                return render(request, 'website/valid-login.html', 
                    { 'user': user })

def mirror(request):
    if request.method == 'GET':
        return render(request, 'website/mirror.html')
