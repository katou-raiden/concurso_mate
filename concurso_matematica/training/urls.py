from django.urls import path
from .views import *

urlpatterns = [
    path('', training_view, name='training'),
    path('exercise/', exercises_view, name='exercise'),
]