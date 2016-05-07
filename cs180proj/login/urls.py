from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib.auth import views as django_views
 
urlpatterns = patterns('',
    #url(r'^$', 'django.contrib.auth.views.login'),
    url('^$', django_views.login),
    url(r'^logout/$', logout_page),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    #url(r'^accounts/login/$', django_views.login),
    url(r'^accounts/login/$', django_views.login),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home), #FIXME: Causes warning about 1.10 compatability?

    #url(r'^login/$', login),
    #url(r'^login/$', views.login_user, name = 'login_user'),

)
