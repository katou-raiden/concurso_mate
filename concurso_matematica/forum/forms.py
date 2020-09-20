from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta():
        model = Post

        exclude = ['fecha']

class AnswerForm(forms.Form):
    content = forms.Textarea()


class ComentForm(forms.Form):

    contenido = forms.CharField(max_length=255)

