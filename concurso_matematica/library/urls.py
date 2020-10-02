from django.urls import  path
from .views import *

urlpatterns = [
    path('', main_view, name='library'),
    path('videos/', videos_gallery_view, name='videos'),
    path('history/', history_post_view, name='history'),

]