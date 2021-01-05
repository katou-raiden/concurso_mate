from django.http.response import HttpResponse, HttpResponseRedirect

from django.forms import formset_factory
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import Completed_ExerciseForm, ExerciseForm, SugestionForm
from django.db.models import F
from django.contrib import messages
from django.shortcuts import reverse


#for htmltopdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def is_authenticated(view):
    def wrapper(request, pk):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, 'No esta autenticado, primero debe loguearse')
            return view(request, pk)
        else:
            return view(request, pk)

    return wrapper

def is_role(role):
    def wrapper1(view):
        def wrapper2(request, pk):
            if hasattr(request.user, role):
                return view(request, pk)
            else:
                messages.add_message(request, messages.ERROR, 'Primero debe ser ' + role + ' para acceder a esta funcionalidad.')
                return view(request, pk)
        return wrapper2
    return wrapper1

def main_view(request):
    
    return render(request, 'training/main.html')


def test_view(request, level):
    test = Level.objects.filter(name=level)[0].test
    exercises = Exercise.objects.filter(test=test)
    total_exercises = len(exercises)
    print('este es el total : ' + str(total_exercises))
    ExercisesForm = formset_factory(Completed_ExerciseForm, extra=total_exercises)
    formset = ExercisesForm()
    gen_forms = (lambda :  (form for form in formset.extra_forms))()

    if request.method == "POST":
        formset = ExercisesForm(request.POST)
        total = 0

        if formset.is_valid():

            for data in formset.cleaned_data:
                total += data.get('points')
                
            total=total/total_exercises
            Completed_Test.objects.create(student=request.user.student, score=total, test=test)

            print('ALL Created, look up for it!')
    
    def the_next():
        return next(gen_forms)

    return render(request,'training/test.html', context = {
        'exercises': exercises,
        'next_form': the_next,
        'formset' : formset,
        })


def level_view(request, level,topic = None):

    general_levels = Level.objects.all()
    actual_level = Level.objects.get(name = level.capitalize())
    topics = actual_level.topics.all()
    default_topic = actual_level.topics.get(pk=1)
    
    if request.GET.get('topic'):
        topic_name = request.GET.get('topic')
        actual_topic = actual_level.topics.get(name=topic_name)
       
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
        return render(request, 'training/level_main.html',context)



def exercise_detail_view(request,pk):

    form = Completed_ExerciseForm()
    exercise = get_object_or_404(Exercise, pk=pk)

    if request.method == "POST":
        if request.user.is_authenticated:
            
            if hasattr(request.user, 'student'):
                
                if Completed_Exercise.objects.filter(pk=pk, student=request.user.student).exists():
                    messages.add_message(request, messages.ERROR, 'Ya ha completado este ejercicio')
                    
                    return HttpResponseRedirect(reverse('exercise', args=[pk]))
                    
                else:
                    form = Completed_ExerciseForm(request.POST)
            else:
                messages.add_message(request, messages.ERROR, 'Debe ser estudiante para realizar algun ejercicio.')
        else:
            messages.add_message(request, messages.ERROR, 'Debe registrarse para hacer este ejercicio')

       

        if form.is_valid():

            form.save(student = request.user.student, exercise = exercise)
            print('saved the holy form')
            return HttpResponseRedirect(reverse('exercise', args=[pk]))
        else:
            print(form.errors)
   
    
    context = { 'exercise':exercise, 'form':form }
    return render(request, 'training/exercise.html',context=context)

    
def create_exercise_view(request):
    ex_form = ExerciseForm()

    Sugs_formset = formset_factory(SugestionForm, extra=4)

    sugx_formset = Sugs_formset()

    context = {'form':ex_form, 'sugs' : sugx_formset}

    if request.method == 'POST':
        ex_form = ExerciseForm(request.POST)
        sugx_formset = Sugs_formset(request.POST)
        ex_form.save()
        
        if ex_form.is_valid():
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
