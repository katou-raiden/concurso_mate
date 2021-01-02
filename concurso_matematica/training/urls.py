from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='training'),
    path('<str:level>/', level_view, name='level_main' ),
    path('exercise/<int:pk>/', exercise_detail_view, name='exercise'),
    path('<str:level>/<str:topic>/', exercise_list_view, name='exercise_list'),
    path('exercise_post/', exercise_post_view, name='ex_post')
]