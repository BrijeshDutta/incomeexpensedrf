from django.db import models

# Create your models here.

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin )

from rest_framework_simplejwt.tokens import RefreshToken

# Creating custom user manager class which is inheriting from Base User manager class
class UserManager(BaseUserManager):
    
    # Override create user method
    
    def create_user(self,username,email,password=None):
        
         # Simple Checks
         
         if username is None:
             raise TypeError('User should have a user Name - message from the model')

         if email is None:
             raise TypeError('User should have an Email id  - message from the model')
         
         # User Object created to set values
         
         user = self.model(username =username, email = self.normalize_email(email))
         user.set_password(password)
         
         # Save the user object in DB
         
         user.save()
         
         return user
         
    # Override create_superuser method
    
    def create_superuser(self,username,email,password=None):
        
         # Simple Checks
         
         if password is None:
             raise TypeError('Password should not be none from model')
         
         user = self.create_user(username, email,password)
         user.is_superuser = True
         user.is_staff = True
         user.save()
         return  user

# Inherits from AbstractBaseUser and Permission Mixin

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']
    
    # Need to tell django how to handle such objects
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        
    
    
    
         
         
