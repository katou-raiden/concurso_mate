from django.db import models
from django.contrib.auth.models import User
from core.models import Tag

# Create your models here.

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.name


class Video(models.Model):
    tag = models.ManyToManyField(Tag, related_name='videos', null=True, blank=True)
    title = models.CharField(max_length=75)
    description = models.TextField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    voted = models.ManyToManyField(User, related_name='video_voted')
    video = models.FileField(upload_to='library/video/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    playlist = models.ForeignKey(Playlist, related_name='videos', on_delete=models.CASCADE, null=True,blank=True, default='0')

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return self.title

class HistoryPost(models.Model):
    tag = models.ManyToManyField(Tag, related_name='history_posts')
    title = models.CharField(max_length=50)
    date_pub = models.DateTimeField(auto_now_add=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, null=True)
    content = models.TextField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    voted = models.ManyToManyField(User, related_name='history_voted')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history_posts')
    image = models.ImageField(null=True, blank=True, upload_to='library/history/imgs')
    
    def __str__(self):
        return self.title

class Comment_History(models.Model):
    user = models.ForeignKey(User , related_name='history_comments', on_delete=models.CASCADE)
    content = models.CharField( max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    votes_plus = models.IntegerField(default=0)
    votes_minus = models.IntegerField(default=0)
    voted = models.ManyToManyField(User, related_name='comment_history_voted')
    post = models.ForeignKey(HistoryPost, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

class Comment_Video(models.Model):
    user = models.ForeignKey(User , related_name='video_comments', on_delete=models.CASCADE)
    content = models.CharField( max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    votes_plus = models.IntegerField(default=0)
    votes_minus = models.IntegerField(default=0)
    voted = models.ManyToManyField(User, related_name='comment_video_voted')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

class Image(models.Model):
    post = models.ForeignKey(HistoryPost,on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='library/images/')
    
    def __str__(self):
        return self.str(img)

class File(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='files')
    doc = models.FileField(upload_to='library/documents/')

