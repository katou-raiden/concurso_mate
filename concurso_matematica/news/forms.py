from django import forms
from .models import *
from django.core.exceptions import FieldError
from tags_input.fields import TagsInputField
from tags_input.widgets import TagsInputWidget
from core.models import Tag
from tinymce.widgets import TinyMCE
from dal import autocomplete
from core.forms import CoreModelForm

class NoticeFilter(CoreModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.__class__.Meta.not_required:
            self.fields[field_name].required = False
    class Meta:
        model = Notice
        fields = {
            'title' : '__icontains',
            'user': 'exact',
            'tag' : '__in',
        }
        
        widgets = {

            'user' : autocomplete.ModelSelect2(url='user-autocomplete'),
            'tag' : autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        }

        not_required = (
            'title',
            'user',
            'tag',
        )

class formulario(forms.Form):
    tag = TagsInputField(Tag.objects.all(), required=False)

class NoticeForm(forms.ModelForm):
    
    class Meta:
        model = Notice
        fields = (
            'title',
            'content',
            'tag',
        )
        widgets = {
            'tag' : autocomplete.ModelSelect2Multiple(url='tag-create-autocomplete'),
            'content' : TinyMCE(),
        }


class MainCommentForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80, 
        'rows': 30,
        'class': 'w-100' 
        }))
    class Meta:
        model = MainComment
        exclude = ['upvotes', 'downvotes', 'date_mod', 'date_pub','notice','user']


class SubCommentForm(forms.ModelForm):
    
    class Meta:
        model = SubComment
        exclude = ['upvotes', 'downvotes', 'date_mod', 'date_pub', 'main_comment','user']