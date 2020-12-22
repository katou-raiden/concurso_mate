from django import forms
from .models import *


class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        exclude = ['upvotes', 'date_created', 'date_updated', 'downvotes', 'user','reference']


class MainCommentForm(forms.ModelForm):

    class Meta:
        model = MainComment
        exclude = ['upvotes', 'downvotes', 'date_mod', 'date_pub','notice','user']


class SubCommentForm(forms.ModelForm):

    class Meta:
        model = SubComment
        exclude = ['upvotes', 'downvotes', 'date_mod', 'date_pub', 'main_comment','user']