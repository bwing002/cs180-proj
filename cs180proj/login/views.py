from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
#from birthdayreminder.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#views.py
from login.forms import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
    	username = request.POST['username']
    	password = request.POST['password']
	user = authenticate(username=username, password = password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/')#request.REQUEST.get('next',''))
    return render(request,'login/login.html', context_instance=RequestContext(request))
@login_required(login_url='/login/')

def post_list(request):
    return render(request, 'login/post_list.html', {})


