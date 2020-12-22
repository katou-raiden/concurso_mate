from django.db import models

# Create your models here.

LEVELS = ('Introductorio' , 'Intermedio' , 'Avanzado' , 'Experto')


class Exercise(models.Model):
    name = models.CharField(max_length=75)
    question = models.TextField()
    qualification_rule = models.TextField()
    topic = models.ForeignKey(Topic, related_name='exercises')
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=75)
    questions = models.ForeignKey(Exercise, related_name='test')

    def __str__(self):
        return self.name
    

class Topic(models.Model):
    name = models.CharField(max_length=75)
    
    def __str__(self):
        return self.name