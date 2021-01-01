from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Exercise
from .forms import Completed_ExerciseForm

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
    form = Completed_ExerciseForm()
    context = {'exercise':exercise, 'form':form}

    if request.method == 'POST':
        form = Completed_ExerciseForm(request.POST)
        s = form.save(commit=False)
        s.name = exercise.name
        s.user = request.user
        s.save()
        exercise.times_solved += 1
        exercise.save()
        # Crear la Succes View Como mejor estimes, eso lo veo mas como un tema de Frontend no se si redireccionar
        # para la lista de ejercicios o para otro lugar tu decide
        return HttpResponse('Todo Bien')
    else:
        return render(request, 'training/exercise.html',context=context)

    
    


    

