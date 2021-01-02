from django.http.response import HttpResponse
from django.forms import formset_factory
from django.shortcuts import redirect, render, get_object_or_404
from .models import Exercise, Sugestion, Level, Topic
from .forms import Completed_ExerciseForm, ExerciseForm, SugestionForm

#for htmltopdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def main_view(request):
    
    return render(request, 'training/main.html')

def level_view(request, level):
    
    topic = request.GET.get('topic', Topic.objects.first().name or None)
    exercises = Exercise.objects.filter(topic__level__name = level, topic__name = topic)
    levels = Level.objects.all()
    level = levels.filter(name=level)
    context = {
        
        'level': level,
        'levels': levels,
        'exercises': exercises,
        }

    if topic:
        context.update({'topic': topic })
    else:
        context.update({'topic': 'NO HAY TOPICO !!' })

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

    
def create_exercise_view(request):
    ex_form = ExerciseForm()

    Sugs_formset = formset_factory(SugestionForm, extra=4)

    sugx_formset = Sugs_formset()

    context = {'form':ex_form, 'sugs' : sugx_formset}

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
        
        return render(request, 'training/create_exercise.html', context=context)

    
def render_pdf_view(request,pk):
    template_path = 'training/pdf_render.html'
    exercise = get_object_or_404(Exercise, pk = pk)
    name = exercise.name
    sugs = Sugestion.objects.filter(exercise=exercise)
    context = {'exercise': exercise,'sugs':sugs}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=name'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
