from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from login.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    embedURL = models.URLField(max_length=200, null=True,blank=True)
    retweeted = models.ManyToManyField(UserProfile, related_name ='retweeted_by')
    tags = models.CharField(max_length=50,null=True,blank=True)
    created_date = models.DateTimeField(
          blank=True,null=True)
    published_date = models.DateTimeField(
          blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    embedURL = models.URLField(max_length=200, null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text

