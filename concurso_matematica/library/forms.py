from django import forms

class CommentForm(forms.ModelForm):

    class Meta():
        exclude = [
            'date_created',
            'date_modified',
            'votes_plus',
            'votes_minus',
            'post',
            'user',
        ]