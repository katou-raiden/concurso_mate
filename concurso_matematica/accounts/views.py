from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def login_view(request):
    
    if request.method == "POST":
        #obtengo username y password del diccionario de POST

        username = request.POST.get('username')
        password = request.POST.get('password')
        # autentico contra todos los backends de autentificacion
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #ligo la sesion del request a la instancia del usuario autentificado
            login(request, user)
            return redirect('home')
        else:
            #mensaje al contexto global por si las credenciales son erroneas
            messages.error(request, 'Usuario o contransenna incorrectos')

    #no hace falta contexto ya que obtengo directamente las credenciales un form personalizado

    return render(request, 'accounts/login.html', {})

def logout_view(request):
    #borro todos los datos de la sesion del request
    logout(request)
    return HttpResponse('You have logged out successfully')

def signUp_view(request):
    #los tres formularios de los tres modelos principales de cuenta de usuario
    user_form = UserForm()
    professor_form = ProfessorForm()
    student_form = StudentForm()
    profile_form = ProfileForm()

    if request.method == "POST":
        
        #si el envio de datos es por post, relleno todos los formularios con su 
        #respectiva info

        user_form = UserForm(request.POST)
        professor_form = ProfessorForm(request.POST)
        student_form = StudentForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid():
            print('usuario valido')
            #Si se rellenaron todos los campos necesarios correctamente del modelo 
            #usuario, entonces estamos listos para proceder con las extensiones del mismo
            #El primero que tenga informacion proveida y correcta, es el procesado

            if professor_form.is_bound and professor_form.is_valid():
                #profesor tiene datos y son correctos (literalmente)

                
                new_user = user_form.save(commit=False)
                new_user.set_password(request.POST.get('password'))
                new_user.save()

                if (profile_form.is_valid()):
                    new_profile = profile_form.save(commit=False)
                    new_profile.user = new_user

                #en estas tres lineas aseguro que la instancia user este salvada para
                #que la extension tenga su referencia asegurada en la bd
                new_professor = professor_form.save(commit=False)
                new_professor.user = new_user
                new_professor.save()
                #modelo extendido salvado con exito y procedemos a la redireccion
                return HttpResponse('Registrado con exito')
            
            elif student_form.is_bound and student_form.is_valid():
                #Mismos procedimientos
                new_user = user_form.save(commit=False)
                new_user.set_password(request.POST.get('password'))
                new_user.save()

                if (profile_form.is_valid()):
                    new_profile = profile_form.save(commit=False)
                    new_profile.user = new_user

                new_student = student_form.save(commit=False)
                new_student.user = new_user
                new_student.save()

                return HttpResponse('Registrado con exito')


    context = {
        'user_form' : user_form,
        'professor_form': professor_form,
        'student_form': student_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/signup.html', context)
        
