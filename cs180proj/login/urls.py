from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib.auth import views as django_views
from . import views 
urlpatterns = patterns('',
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^login/$', django_views.login),
    #url(r'follow', views.follow_user, name = 'follow_user'),
)
