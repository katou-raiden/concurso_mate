from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='training'),
    path('<str:level>/', category_view, name='category' ),
    path('<str:level>/<str:topic>/', exercise_list_view, name='exercise_list'),
    path('exercise/<int:pk>/', exercise_detail_view, name='exercise'),
]