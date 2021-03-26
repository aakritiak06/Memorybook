from django import forms
from django.forms import ModelForm
from .models import *




class EditorForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title','body','difficulty','difficulty_rating']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']        