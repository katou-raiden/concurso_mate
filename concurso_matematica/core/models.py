from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,blank=True, null=True, default='')
    
    def __str__(self):
        return self.name




