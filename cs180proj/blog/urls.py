from django.conf.urls import url, patterns, include 
from . import views
urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    #url(r'^blog/$',post_list),
    #url(r'^post/new/$',views.post_new, name='post_new'),
    #url(r'^accounts/login/$', views.login, name = 'login'),
    #url(r'^accounts/login$', 'django.contrib.auth.views.login'),
]
