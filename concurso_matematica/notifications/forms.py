from django import forms
from .models import *
class NotificationForm(forms.ModelForm):
    
    class Meta:
        model = Notification
        fields = (
            'message',
            'role',
            'code',
        ) 