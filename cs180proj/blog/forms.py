import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from login.models import UserProfile
from .models import Post
class PostForm(forms.ModelForm):
		class Meta:
			model = Post
			fields = ('title', 'text')