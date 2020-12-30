from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='training'),
    path('exercise/', exercise_detail_view, name='exercise'),
    
]