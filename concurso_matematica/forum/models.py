from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    #tag = models.ForeignKey('', on_delete=models.CASCADE, related_name='post', null=True)
    content = models.TextField(default='',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    content = models.TextField(default='',null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=75)
    votes_plus = models.IntegerField(default=0)
    votes_minus = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers', null=True)
    

    def __str__ (self):
        return self.content

class Comment(models.Model):
    content = models.TextField(default='',null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    votes_plus = models.IntegerField(default=0)
    votes_minus = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.content


