from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index.html$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^signup.html$', views.signup, name='signup'),
    # url(r'^createuser.html$', views.createuser, name='createuser'),
]
