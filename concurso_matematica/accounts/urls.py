from .views import *
from django.urls import path
urlpatterns = [
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name='logout'),
  path('sign-up/', signUp_view, name='signup'),

]