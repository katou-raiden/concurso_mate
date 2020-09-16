from django.shortcuts import render
from .models import *
# Create your views here.

def new_view(request):

    news = Notice.objects.all()[:6]
    context = {
        'news' : news,
    }
    return render(request, 'news/new.html', context)