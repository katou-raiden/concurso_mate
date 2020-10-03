from django.db import models
from forum import models as forum_models
from news import models as news_models
from library import models as library_models




class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,blank=True, null=True, default='')
    notice = models.ManyToManyField(news_models.Notice, related_name='tags')
    post = models.ManyToManyField(forum_models.Post, related_name='tags')
    history_post = models.ManyToManyField(library_models.HistoryPost , related_name='tags')

    def __str__(self):
        return self.name