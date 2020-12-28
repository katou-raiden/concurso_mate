from django.shortcuts import render

# Create your views here.

def training_view(request):
    ctx = {}
    return render(request, 'training/training_main.html', ctx)

def exercises_view(request):
    ctx = {}
    return render(request, 'training/exercise.html', ctx)