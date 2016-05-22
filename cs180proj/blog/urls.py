from django.conf.urls import url, patterns, include 
from . import views
urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    #url(r'^blog/$',post_list),
    #url(r'^post/new/$',views.post_new, name='post_new'),
    #url(r'^accounts/login/$', views.login, name = 'login'),
    #url(r'^accounts/login$', 'django.contrib.auth.views.login'),
]
