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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', django_views.login),#
    url(r'^$', post_list),
    url(r'^home/$', home), #FIXME: Our home is the login screen?
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^register/login/$', django_views.login), #Redirects to /login/
    url(r'^logout/$', logout_page),
    url(r'', include('blog.urls')),
    url(r'', include('login.urls')),
    #url(r'',home),
    url(r'^accounts/profile/$', profile), #FIXME:Now directs to the post_list, is this what we have as a profile?
    url(r'^login/$', django_views.login),
    #url(r'^login/$', 'admin.auth.views.login'), #Old, not sure where this references, but it doesn't exist
]
