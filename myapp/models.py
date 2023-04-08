from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from. managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    first_name= models.CharField(max_length=250)
    email= models.EmailField(_('Email Address'),unique=True)
    mobile= models.CharField(max_length=10)
    status= models.BooleanField(default=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['mobile']
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    # is_superuser=models.BooleanField(default=False)
    object = CustomUserManager()
