from django.shortcuts import render
from .models import *
# Create your views here.

def new_view(request, pk):

    new = Notice.objects.get(pk=pk)
    context = {
        'new' : new,
    }
    return render(request, 'news/new.html', context)

def list_news_view(request):
    context = {
        
    }
    return render(request, 'news/new.html', context)
