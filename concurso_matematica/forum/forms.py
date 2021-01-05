from django import forms
from .models import Post
from tinymce.widgets import TinyMCE
from core.forms import CoreModelForm
from dal import autocomplete
class PostFilter(CoreModelForm):

    class Meta:

        model = Post

        fields = {
            'title' : '__icontains',
            'user': '__exact',
            'tag' : '__in',
        }
        labels = {
            'tag' : 'Etiquetas'
        }
        widgets = {
            'tag' : autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
            'user' : autocomplete.ModelSelect2(url='user-autocomplete'),
        }

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'tag',
        )
        widgets = {
            'tag' : autocomplete.ModelSelect2Multiple(url='tag-create-autocomplete')
        }

class AnswerForm(forms.Form):
    content = forms.Textarea()


class ComentForm(forms.Form):

    contenido = forms.CharField(max_length=255)

