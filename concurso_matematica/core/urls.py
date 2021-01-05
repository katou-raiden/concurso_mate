from .views import *
from django.urls import path, re_path 
urlpatterns = [
    path('home/', home_view, name="home"),
    path('about/', about_view, name="about"),
    path('tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),
    path('tag-create-autocomplete/', TagAutocomplete.as_view(create_field='name'), name='tag-create-autocomplete'),
    path('user-autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete')
]