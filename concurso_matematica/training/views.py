from django.shortcuts import render, get_object_or_404
from .models import Exercise

# Create your views here.

def main_view(request):
    return render(request, 'training/main.html')

def category_view(request, level):
    context = {'level': level}
    return render(request, 'training/category.html', context=context)

def exercise_list_view(request, level, topic):
    exercises = Exercise.objects.filter(level == level and topic == topic)

    context = {'exercises':exercises}

    return render(request, 'training/exercises.html', context=context)

def exercise_detail_view(request,pk):
    exercise = get_object_or_404(Exercise, pk = pk)

    context = {'exercise':exercise}
    pass


    

