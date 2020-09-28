from .views import *
from django.urls import path
urlpatterns = [
    path('<int:pk>/', new_view, name="new"),
    path('', list_news_view, name="news"),
    path('add-new', add_new_view, name='add_new')
]