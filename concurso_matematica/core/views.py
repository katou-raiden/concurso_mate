from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from news.models import *
from dal import autocomplete
from .models import Tag
from django.contrib.auth.models import User
from django.template import Template, Context
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

class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
       
        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
   
        qs = User.objects.all()

        if self.q:
            qs = qs.filter(username__istartswith=self.q)

        return qs
class Algo():
    pass