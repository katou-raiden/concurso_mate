from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=30, default="")
    text = models.TextField(null=True, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    reference = models.URLField(null=True, blank=True, default="")
    image = models.ImageField(upload_to='news/images', null=True)
    upvotes = models.IntegerField(null=False, blank=False, default=0)
    downvotes = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.title + ' - ' + str(self.date_created)
    


