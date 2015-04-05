from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include('website.urls', namespace='website')),
]
