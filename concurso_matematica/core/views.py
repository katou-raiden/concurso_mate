from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import *
# Create your views here.


def home_view(request):
    news = Notice.objects.all()[:6]
    context = {
        'news':news,
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    context = {

    }
    return render(request, 'core/about.html', context)