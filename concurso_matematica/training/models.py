from django.db import models
from accounts.models import Student


# Create your models here.

LEVELS = ('Introductorio' , 'Intermedio' , 'Avanzado' , 'Experto')

class Level(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=75)
    level = models.ForeignKey(Level, default=None, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return self.name
class Test(models.Model):

    name = models.CharField(max_length=75)
    level = models.OneToOneField(Level, default = (Level.objects.first().pk or None), on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class Completed_Test(models.Model):

    student = models.ForeignKey('accounts.Student', default=None, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, default=None, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


class Exercise(models.Model):


    name = models.CharField(max_length=75)
    question = models.TextField()
    qualification_rule = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE , related_name='exercises')
    times_visited = models.IntegerField(default=0,blank=True, null=True)
    test = models.ForeignKey(Test, default=None, null=True, blank=True, on_delete=models.CASCADE, related_name='exercise')

    def __str__(self):
        return self.name


class Sugestion(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sugestions')
    time = models.IntegerField(default=0)
    text = models.TextField()

    def __str__(self):
        return self.text



class Completed_Exercise(models.Model):

    possible_scores = list(zip(range(1,8), range(1,8)))
    exercise = models.ForeignKey(Exercise, default=None, on_delete=models.CASCADE)
    points = models.IntegerField(default=0, choices=possible_scores)
    student = models.ForeignKey('accounts.Student', on_delete = models.CASCADE, related_name='completed_exercises')
    

