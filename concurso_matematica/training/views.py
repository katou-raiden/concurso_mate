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

def test_view(request):
    form = Completed_ExerciseForm(request.POST)
    return render(request,'training/ex_post.html',context={'form':form})


def level_view(request, level,topic = None):

    general_levels = Level.objects.all()
    actual_level = Level.objects.get(name = level.capitalize())
    topics = actual_level.topics.all()
    default_topic = actual_level.topics.get(pk=1)
    
    if request.GET.get('topic'):
        topic_name = request.GET.get('topic')
        actual_topic = actual_level.topics.get(name=topic_name)
        print('Con topic marcado '+actual_topic)
        exercises = Exercise.objects.filer(topic = actual_topic)
        context = {
            #nivel en que estas
            'actual_level': actual_level,
            'actual_topic':actual_topic,
            'topics':topics,
            'exercises':exercises,
            'general_levels':general_levels
        }
        return render(request, 'training/level_main.html',context)
    else:
        exercises = Exercise.objects.filter(topic = default_topic)
        context = {
            #nivel en que estas
            'actual_level': actual_level,
            'actual_topic':default_topic,
            'topics':topics,
            'exercises':exercises,
            'general_levels':general_levels
        }
        print('Nivel Actual ')
        print(actual_level)
        print('Topic por default ')
        print(default_topic)
        print('Todos los topics ')
        print(topics)
        print('Ejercicios ')
        print(exercises)
        print('Todos los niveles ')
        print(general_levels) 
        return render(request, 'training/level_main.html',context)


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
