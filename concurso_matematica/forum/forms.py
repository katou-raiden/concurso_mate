from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta():
        model = Post

        exclude = ['date_pub', 'date_mod', 'user','voted','section']

class AnswerForm(forms.Form):
    content = forms.Textarea()


class ComentForm(forms.Form):

    contenido = forms.CharField(max_length=255)

