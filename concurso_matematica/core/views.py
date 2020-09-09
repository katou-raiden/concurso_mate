from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_view(request):
    context = {

    }
    return render(request, 'core/home.html', context)

def about_view(request):
    context = {

    }
    return render(request, 'core/about.html', context)