from django.urls import path
from . import views

urlpatterns = [
    path('edit/post/<int:pk>', views.edit_post_view, name='edit_post'),
    path('edit/hpost/<int:pk>', views.edit_Hpost_view, name='edit_hpost'),
    
]