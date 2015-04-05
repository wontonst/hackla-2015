from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^users/', views.UserList.as_view(), name='list_of_users'),
    url(r'^tokens/', views.TokenList.as_view(), name='list_of_tokens'),
    url(r'^moods/', views.MoodList.as_view(), name='list_of_moods'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
