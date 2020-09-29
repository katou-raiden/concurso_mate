from django.db import models
from forum import models as forum
from news import models as news
from library import models as library

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,blank=True, null=True, default='')
    notice = models.ManyToManyField(news.Notice, related_name='tags')
    post = models.ManyToManyField(forum.Post, related_name='tags')
    history_post = models.ManyToManyField(library.HistoryPost , related_name='tags')

    def __str__(self):
        return self.name
