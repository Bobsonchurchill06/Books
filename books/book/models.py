from django.contrib.auth.models import User
from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=250, blank=True, null=True, unique=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField()
    joined_date = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    
    
class Books(models.Model):
    book_name = models.CharField(max_length=50, blank=False, null=False, unique=False)  
    description = models.CharField(max_length=250)
    user = models.ForeignKey(Users, related_name='user', unique=False, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, related_name='creator_cbook', on_delete= models.DO_NOTHING, null=True)
    modified_by = models.ForeignKey(Users, related_name='+', on_delete=models.DO_NOTHING, null=True)

