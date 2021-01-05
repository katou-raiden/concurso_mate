import os, django, sys
sys.path.append('/home/l0new0lf/Documents/Projects/concurso_matematica/concurso_matematica/concurso_matematica')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concurso_matematica.settings')
django.setup()

### My code Here ###

from django.template import Context, Template
from django import forms
from news.models import Notice
from django.core.exceptions import ValidationError
from django.urls import reverse
from typing import Any, Literal, List
from django.template import Library



print(Template('Hello There {{ martin }}').render(Context({'martin': 'Arturo'}), ))
print(reverse('tag-autocomplete'))

register = Library()

a, b = 10, 15

def pythonf(): return (lambda: a, lambda: b) [a > b]()
    
import os
from dateutil import parser
from datetime import datetime, date, timezone, timedelta
import time
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
from django.forms import Form, CharField
from core.models import Tag
from news import forms
from news.models import Notice
import random, string
import math

class AForm(Form):
    name = CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

form = AForm(dict())

news = Notice.objects.all()
tags = Tag.objects.all()

print(news.filter(title='Cree este', tag__in = tags))

#print(string.ascii_uppercase, string.digits)

def random_dict(length=8):
    x = 1
    dict_ = dict()
    while x <= length:
        x+=1
        dict_.setdefault(
            ''.join(random.choices(string.ascii_lowercase,k=random.randint(6,length))),
            math.floor(random.random()*10000)
        )
    return dict_

d = random_dict()
dc = d.copy()

for key in d.keys():
    value = dc.pop(key)
    dc.setdefault(key+'__in', value)
    
print(d)
print(dc)





