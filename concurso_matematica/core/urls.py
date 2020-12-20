from .views import *
from django.urls import path
urlpatterns = [
    path('home/', home_view, name="home"),
    path('about/', about_view, name="about"),
]