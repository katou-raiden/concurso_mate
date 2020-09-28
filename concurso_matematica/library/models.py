from django.db import models
from django.contrib.auth.models import User
from core.models import Tag

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    video = models.FileField(upload_to='library/video/')

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.title

class HistoryPost(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history_posts')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User , related_name='history_comments', on_delete=models.CASCADE)
    content = models.CharField( max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(HistoryPost, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
    
class Image(models.Model):
    post = models.ForeignKey(HistoryPost,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='library/images/')
    
    def __str__(self):
        return self.str(img)
    
