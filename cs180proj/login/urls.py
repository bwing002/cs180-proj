from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib.auth import views as django_views
 
urlpatterns = patterns('',
    url(r'^$', django_views.login),
    url(r'^logout/$', logout_page),
    #url(r'^accounts/login/$', django_views.login),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^login/$', django_views.login),
)
