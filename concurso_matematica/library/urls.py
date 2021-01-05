from django.urls import  path
from .views import *

urlpatterns = [
    path('videos/', videos_gallery_view, name='videos'),
    path('videos/<int:pk>', video_detail_view, name = 'video_detail'),
    path('videos/post-video', video_post_view, name = 'video_post'),
    path('history/', history_view, name='history'),
    path('create-history/', create_history_view, name='create-history'),
    path('edit-history/', edit_history_view, name='edit-history'),
    path('history/<int:pk>', history_post_view, name='history_post'),
    path('downloads/', downloads_view, name="downloads")

]