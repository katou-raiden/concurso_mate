from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *


# Create your views here.
def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("""Se ha logueado el usuario "%s" correctamente!!
                <a href="/accounts/logout">logout</a>
            """ % (user.username))
        else:
            return HttpResponse('Usuario o contrasennas incorrectos')

    return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponse('You have logged out successfully')

def signUp_view(request):
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)  
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            print(new_user.password)
            new_user.set_password(request.POST.get('password'))
            new_user.save()
            return HttpResponse('Registrado con exito')
    
    context = {
        'user_form' : user_form,
    }
    return render(request, 'accounts/signup.html', context)
        
