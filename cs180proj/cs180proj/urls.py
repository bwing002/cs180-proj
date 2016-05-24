"""cs180proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from login.views import *
from django.contrib.auth import views as django_views
from blog.views import *
#from cs180proj.index import views

urlpatterns = [
    url(r'^$', index), #Homepage
    url(r'^admin/', admin.site.urls), #Default
    url(r'', include('blog.urls')),
    url(r'', include('login.urls')),
    url(r'^accounts/profile/$', profile), #Put these in profile
    url(r'^accounts/profile/edit$', edit_profile),
    url(r'^accounts/profile/(?P<viewusername>[\w.@+-]+)/$', view_profile),
    url(r'^accounts/profile/(?P<viewusername>[\w.@+-]+)/follow/$', follow_user),
    url(r'^accounts/profile/(?P<viewusername>[\w.@+-]+)/unfollow/$', unfollow_user),
]
