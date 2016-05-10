from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
