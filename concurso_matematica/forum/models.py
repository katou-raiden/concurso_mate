from django.db import models
from core.models import Tag
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    tag = models.ManyToManyField(Tag,related_name='tags',blank=True,null=True)
    title = models.CharField(max_length=150)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    content = models.TextField(default='',null=True)
    voted = models.ManyToManyField(User, related_name='post_voted',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    section = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    content = models.TextField(default='',null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=75)
    votes_plus = models.IntegerField(default=0)
    votes_minus = models.IntegerField(default=0)
    voted = models.ManyToManyField(User, related_name='answer_post_voted',blank=True)
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
    voted = models.ManyToManyField(User, related_name='comment_post_voted',blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    answer = models.ForeignKey(Answer, blank=True, on_delete=models.CASCADE, related_name='comments', null=True, default=None)

    def __str__(self):
        return self.content

