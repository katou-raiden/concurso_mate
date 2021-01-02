from django.http.response import HttpResponse
from django.forms import formset_factory
from django.shortcuts import redirect, render, get_object_or_404
from .models import Exercise
from .forms import Completed_ExerciseForm, ExerciseForm, SugestionForm

# Create your views here.

def main_view(request):
    
    return render(request, 'training/main.html')

def level_view(request, level):
    exercises = Exercise.objects.filter(level = level, topic = request.GET.get('topic', None))
    context = {
        'level': level,
        'exercises': exercises,
        }
    return render(request, 'training/level_main.html', context=context)

def exercise_list_view(request, level, topic):
    

    context = {}
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

    
def exercise_post_view(request):
    ex_form = ExerciseForm()

    Sugs_formset = formset_factory(SugestionForm, extra=4)

    sugx_formset = Sugs_formset()

    context = {'ex':ex_form, 'sugs' : sugx_formset}

    if request.method == 'POST':
        ex_form = ExerciseForm(request.POST)
        sugx_formset = Sugs_formset(request.POST)

        if ex_form.is_valid() and sugx_formset.is_valid():
            ex = ex_form.save()

            for form in sugx_formset:
                s = form.save(commit = False)
                s.exercise = ex
                s.save()
        
        return HttpResponse('Todo Bien')
    
    else:
        
        return render(request, 'training/ex_post.html', context=context)

    

