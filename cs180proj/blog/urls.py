from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.login, name = 'login',
]
