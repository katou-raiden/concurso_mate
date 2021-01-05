from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    """
    Class for defining Notifications, codes are the following:
    1 - Critical
    2 - Error
    3 - Warning
    4 - Info
    """
    message = models.TextField(max_length=255, default='')
    users = models.ManyToManyField(User, related_name='notifications')
    role = models.TextField(max_length=12, default='all')
    seen = models.BooleanField(default=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    code = models.SmallIntegerField(default=3)

    