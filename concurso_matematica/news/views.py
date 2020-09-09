from django.shortcuts import render

# Create your views here.

def new(request):
    context = {

    }
    return render(request, 'news/new.html', context)