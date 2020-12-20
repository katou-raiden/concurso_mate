<<<<<<< HEAD
from django.db import models
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,blank=True, null=True, default='')
    
    def __str__(self):
=======
from django.db import models
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,blank=True, null=True, default='')
    
    def __str__(self):
>>>>>>> d45844c55919cf3995c6e9f1800748e4cf58f610
        return self.name