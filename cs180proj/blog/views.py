from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
from .models import Post
from .forms import PostForm, CommentForm
from login.models import UserProfile
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import User

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("www.youtube.com")

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def search_tags(request):
    if request.method == "POST":
        tagin = request.POST.get('tag',None)
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/tagged_posts.html', {'posts': posts, 'tagin':tagin})
    return redirect('/blog/')

def tag_list(request, tagin):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/tagged_posts.html', {'posts': posts, 'tagin':tagin})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            if request.POST['embedURL']:
                post.embedURL = form.cleaned_data['embedURL']
            if request.POST['tags']:
                post.tags = form.cleaned_data['tags']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.POST['embedURL']:
                post.embedURL = form.cleaned_data['embedURL']
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def retweet(request, pk):
    post = get_object_or_404(Post, pk=pk)
    userprofile = UserProfile.objects.get(user=request.user)
    post.retweeted.add(userprofile)
    return redirect('/post/'+pk)

