from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UpdateInformation
from login.models import UserProfile
from datetime import *
from blog.models import Post
from blog.forms import PostForm, CommentForm

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
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
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

def index(request):
    if request.user.is_authenticated():
	    return redirect('/accounts/profile/')
    return render_to_response(
        'home/index.html',context_instance=RequestContext(request))
 
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

def profile(request):
  user=request.user
  posts = Post.objects.filter(author=user)
  return render(request, 'login/profile.html', {'user':user,'posts':posts})

#def edit_profile(request):
#  return render(request, 'login/edit_profile.html', {})

def edit_profile(request):
    if request.method == "POST":
        form = UpdateInformation(request.POST)
        userprofile = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user = request.user
            if request.POST['first_name']:
                user.first_name = request.POST['first_name']
            if request.POST['last_name']:
                user.last_name = request.POST['last_name']
            if request.POST['user_sex']:
                user_sex = form.cleaned_data['user_sex']
                userprofile.user_sex = user_sex
            if request.POST['nickname']:
                nickname = form.cleaned_data['nickname']
                userprofile.nickname = nickname
            if request.POST['biography']:
                biography = form.cleaned_data['biography']
                userprofile.biography = biography
            if request.POST['profile_picture_url']:
                userprofile.profile_picture_url = form.cleaned_data['profile_picture_url']
            userprofile.save()
            user.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
    	userprofile = UserProfile.objects.get(user=request.user)
        form = UpdateInformation()

	variables = RequestContext(request, {
    'form': form,'userprofile': userprofile,
    })
    return render_to_response('login/edit_profile.html',{'userprofile':userprofile,'form':form},RequestContext(request))            
        
def view_profile(request, viewusername):
    if User.objects.filter(username=viewusername).exists():
        userprofile = UserProfile.objects.get(user=User.objects.get(username=viewusername))
        user = User.objects.get(username=viewusername)
        posts = Post.objects.filter(author=user)
        return render(request, 'login/view_profile.html', {'userprofile':userprofile,'user':user, 'posts':posts})
#CREATE A WEBPAGE FOR A PROFILE DOES NOT EXIST 
    return render(request, 'login/view_profile.html', {})
        
def follow_user(request, viewusername):
	temp = UserProfile.objects.get(user=User.objects.get(username=viewusername))
	user = User.objects.get(username=viewusername)
	userprofile = UserProfile.objects.get(user=request.user)
	userprofile.follows.add(user.userprofile)
#	return render(process_request, 'login/view_profile.html', {'userprofile':userprofile,'user':user})
	return redirect('/accounts/profile/'+viewusername)
        
def unfollow_user(request, viewusername):
	temp = UserProfile.objects.get(user=User.objects.get(username=viewusername))
	user = User.objects.get(username=viewusername)
	userprofile = UserProfile.objects.get(user=request.user)
	userprofile.follows.remove(user.userprofile)
#	return render(request, 'login/view_profile.html', {'userprofile':userprofile,'user':user})
	return redirect('/accounts/profile/'+viewusername)
       









 
