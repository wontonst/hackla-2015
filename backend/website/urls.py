from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index.html$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^signup.html$', views.signup, name='signup'),
    url(r'^signin.html$', views.signin, name='signin'),
    url(r'^mirror.html$', views.mirror, name='mirror'),
    url(r'^grid.html$', views.grid, name='grid'),
    url(r'^page.html$', views.page, name='page'),
]
