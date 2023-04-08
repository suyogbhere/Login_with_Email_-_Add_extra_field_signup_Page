from django import forms
from.models import *
from django.contrib.auth.forms import UserCreationForm


class Signupform(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput())
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields= ['first_name','email','mobile']