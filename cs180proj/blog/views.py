from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
#from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#def login_user(request):
#    logout(request)
#    username = password = ''
#    if request.POST:
#    	username = request.POST['username']
#    	password = request.POST['password']
#	user = authenticate(username=username, password = password)
#	if user is not None:
#		if user.is_active:
#			auth.login(request, user)
#			return HttpResponseRedirect('/main')
#    return render(request,'blog/login.html', context_instance=RequestContext(request))

#@login_required(login_url='/login/')

def post_list(request):
    return render(request, 'blog/post_list.html', {})


