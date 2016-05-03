from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^accounts/login/$', views.login, name = 'login'),
    #url(r'^accounts/login$', 'django.contrib.auth.views.login'),
]
