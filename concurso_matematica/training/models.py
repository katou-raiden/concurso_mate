from django.db import models


# Create your models here.

LEVELS = ('Introductorio' , 'Intermedio' , 'Avanzado' , 'Experto')



class Topic(models.Model):
    name = models.CharField(max_length=75)
    
    def __str__(self):
        return self.name
class Exercise(models.Model):
    name = models.CharField(max_length=75)
    question = models.TextField()
    qualification_rule = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='exercises')
    level = models.CharField(max_length=20)
    times_visited = models.IntegerField(default=0,blank=True, null=True)
    times_solved = models.IntegerField(default=0,blank=True, null=True)
    related_pdf = models.FileField(upload_to='media/training/pdf', default=None, null=True, blank=True)

    def __str__(self):
        return self.name

class Sugestion(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sugestions')
    time = models.IntegerField(default=0)
    text = models.TextField()

    def __str__(self):
        return self.text

class Test(models.Model):
    name = models.CharField(max_length=75)
    questions = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='test')

    def __str__(self):
        return self.name
