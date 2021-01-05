from django.db import models
from django.contrib.auth.models import User
from news.models import Notice
#from tinymce.models import HTMLField 
from django.core.validators import RegexValidator
# Create your models here.

PROVINCE_REGEX = '48|47|7|45|42|43|51|41|33|32|31|24|23|22|21|46'
PUI_REGEX = None

class Profile(models.Model):

    avatar = models.ImageField(upload_to="users/profile_pictures", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=7, blank=True, default='', null=True)
    private_number = models.CharField(max_length=9, blank=True, default='', null=True)
    province = models.CharField(max_length=15, blank=True, default='', null=True)
    dni = models.CharField(max_length=11, blank='', default='', null=True)
    home_address =models.CharField(max_length=40, default='', blank='', null=True)
    

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="student")
    pui = models.CharField(max_length=20, blank=True, default='')
    grade = models.CharField(max_length=1, blank=True, default='')
    score = models.IntegerField(default=0)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Professor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    institute = models.CharField(max_length=20, blank=True, default='')
    reputation = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class SocialLink(models.Model):
    link = models.URLField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
