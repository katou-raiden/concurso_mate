from django import forms

class PlaylistForm(forms.ModelForm):
    
    class Meta():
        exclude = [
            'user'
        ]

class VideoForm(forms.ModelForm):

    class Meta():
        fields = [
            'title',
            'description',
            'tag',
            'video',
        ]
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