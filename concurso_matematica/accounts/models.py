from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pui = models.CharField(max_length=20, blank=True, default='')
    province = models.CharField(max_length=15, blank=True,default='')
    grade = models.CharField(max_length=1, blank=True, default='')
    phone_number = models.CharField(max_length=9, blank=True, default='')
    private_number = models.CharField(max_length=14, blank=True, default='')
    

class Professor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9, blank=True, default='')
    private_number = models.CharField(max_length=14, blank=True, default='')
    province = models.CharField(max_length=15, blank=True, default='')
    institute = models.CharField(max_length=20, blank=True, default='')

class SocialLink(models.Model):
    link = models.URLField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
