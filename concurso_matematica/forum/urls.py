from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_main_view, name='forum_main'),
    path('detail/<int:id>', views.forum_detail_view, name='forum_detail'),
    path('filter/<int:id>', views.forum_filter_view, name='forum_filter'),
    path('post/', views.forum_post_view, name='forum_post'),
    path('my-posts/', views.my_posts_view, name='my_posts'),
    path('my-posts/edit/<int:id>', views.my_posts_edit_view, name='post_edit'),
]