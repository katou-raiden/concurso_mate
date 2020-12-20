from .views import *
from django.urls import path
urlpatterns = [
    path('', list_news_view, name="news"),
    path('create-notice/', create_notice, name="create-notice"),
    path('<int:pk>/', new_view, name="new"),
    path('upvote_main/<int:pk>/', upvote_main, name='votemain'),
    path('upvote_sub/<int:pk>/', upvote_sub, name='votesub'),
    path('downvote_main/<int:pk>/', downvote_main, name='downmain'),
    path('downvote_sub/<int:pk>/', downvote_sub, name='downsub'),
    path('<tag_name>/', tag_click_view, name='tag_click'),
]