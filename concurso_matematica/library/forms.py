from .models import Comment_History, Comment_Video, Video
from django import forms

class PlaylistForm(forms.ModelForm):
    
    class Meta():
        exclude = [
            'user'
        ]

class VideoForm(forms.ModelForm):
    '''
    tag = models.ManyToManyField(Tag, related_name='videos', null=True, blank=True)
    title = models.CharField(max_length=75)
    description = models.TextField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    voted = models.ManyToManyField(User, related_name='video_voted')
    video = models.FileField(upload_to='library/video/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    playlist = models.ForeignKey(Playlist, related_name='videos', on_delete=models.CASCADE, null=True,blank=True, default='0')
    '''
    class Meta():
        model = Video
        exclude = [
            'up_votes',
            'down_votes',
            'voted',
            'user',
            'playlist',

        ]
class CommentHistoryForm(forms.ModelForm):

    class Meta():
        model = Comment_History
        exclude = [
            'date_created',
            'date_modified',
            'votes_plus',
            'votes_minus',
            'post',
            'user',
        ]

class CommentVideoForm(forms.ModelForm):

    class Meta():
        model = Comment_Video
        exclude = [
            'date_created',
            'date_modified',
            'votes_plus',
            'votes_minus',
            'video',
            'user',
        ]