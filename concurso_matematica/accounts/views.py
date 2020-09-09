from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contransenna incorrectos')

    return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponse('You have logged out successfully')

def signUp_view(request):
    user_form = UserForm()
    professor_form = ProfessorForm()
    student_form = StudentForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        professor_form = ProfessorForm(request.POST)
        student_form = StudentForm(request.POST)

        if user_form.is_valid():
            if professor_form.is_bound and professor_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(request.POST.get('password'))
                new_user.save()
                new_professor = professor_form.save(commit=False)
                new_professor.user = new_user
                new_professor.save()

                return HttpResponse('Registrado con exito')
            
            elif student_form.is_bound and student_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(request.POST.get('password'))
                new_user.save()
                new_student = student_form.save(commit=False)
                new_student.user = new_user
                new_student.save()

                return HttpResponse('Registrado con exito')

    
    context = {
        'user_form' : user_form,
        'professor_form': professor_form,
        'student_form': student_form,
    }
    return render(request, 'accounts/signup.html', context)
        
