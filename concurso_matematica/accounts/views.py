from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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