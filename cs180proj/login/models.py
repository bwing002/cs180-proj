from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    user_sex = models.CharField(max_length=30,blank=True,null=True)
    birth_date = models.DateTimeField(blank=True,null=True)
    join_date = models.DateTimeField(auto_now_add=True, blank=True)
    profile_picture_url = models.ImageField(upload_to='profile_images', blank=True,null=True)
    follows = models.ManyToManyField('UserProfile', related_name ='followed_by')
    
    def __unicode__(self):
    	return self.user.username


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		profile, new = UserProfile.objects.get_or_create(user=instance)