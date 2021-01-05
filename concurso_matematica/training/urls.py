from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='training'),
    path('create_exercise/', create_exercise_view, name='create_exercise'),
    path('exercise/<int:pk>/', exercise_detail_view, name='exercise'),
    #path('exercise_post/', exercise_post_view, name='ex_post'),
    path('exercise_to_pdf/<int:pk>/', render_pdf_view, name='render'),
    path('<str:level>/', level_view, name='level_main' ),
    path('<str:level>/do_test/', test_view, name="test"),
]