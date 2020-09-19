from .views import *
from django.urls import path
urlpatterns = [
    path('<int:pk>/', new_view, name="new"),
    path('', news_view, name="news"),
]