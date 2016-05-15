from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30,blank=True, null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    user_sex = models.CharField(max_length=30,blank=True,null=True)
    birth_date = models.DateTimeField(blank=True,null=True)
    join_date = models.DateTimeField(auto_now_add=True, blank=True)
    profile_picture_url = models.CharField(max_length=200,blank=True,null=True)
