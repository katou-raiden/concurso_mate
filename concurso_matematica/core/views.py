from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {

    }
    return render(request, 'core/home.html', context)

def about_view(request):
    context = {

    }
    return render(request, 'core/about.html', context)