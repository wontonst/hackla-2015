from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['passwd']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        user = User.objects.create_user(email, email, password, first_name = firstname, last_name = lastname) 

        return render(request, 'website/usercreated.html', 
            {'email': email, 
            'firstname': firstname, 
            'lastname': lastname })
    else:
        return render(request, 'website/signup.html', {})

