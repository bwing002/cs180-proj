from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
	url(r'^login/$', views.login_user, name = 'login_user'),
	#url(r'register/$', views.register, name = 'register'),
]
