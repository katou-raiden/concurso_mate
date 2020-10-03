from django.urls import  path
from .views import *

urlpatterns = [
    path('', main_view, name='library'),
    path('videos/', videos_gallery_view, name='videos'),
    path('history/', history_view, name='history'),
    path('history/<int:pk>', history_post_view, name='history_post'),

]