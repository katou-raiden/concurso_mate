from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,blank=True, null=True, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post', null=True)
    content = models.TextField()
    user = models.CharField(max_length=75, default='', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=75)
    votes_plus = models.IntegerField(default=0)
    votes_minus = models.IntegerField(default=0)
    'Related name es el nombre que va a recibir la relacion en el otro modelo'
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return self.content

