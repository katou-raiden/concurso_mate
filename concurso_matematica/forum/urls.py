from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_main_view, name='forum'),
    path('detail/<int:id>', views.forum_detail_view, name='forum_detail'),
    path('filter/<int:id>', views.forum_filter_view, name='forum_filter'),
    path('section/<section>', views.section_view, name="doubts"),
    path('section/<section>/post', views.forum_create_post_view, name = 'post')
    
]