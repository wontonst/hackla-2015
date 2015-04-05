from django.conf.urls import url
from rest_framework.authtoken import views

from . import views

urlpatterns = [
    url(r'^users/', views.users),
    url(r'^tokens/', views.tokens),
    url(r'^moods/', views.moods),
]
