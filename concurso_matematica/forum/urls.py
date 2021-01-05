from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_main_view, name='forum'),
    path('detail/<int:id>/', views.forum_detail_view, name='forum_detail'),
    path('filter/<int:id>/', views.forum_filter_view, name='forum_filter'),
    path('section/<str:section>/', views.section_view, name="section"),
    path('section/<str:section>/create-post/', views.create_post_view, name = 'create-post'),

    
]