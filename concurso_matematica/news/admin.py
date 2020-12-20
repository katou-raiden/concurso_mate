from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Notice)
admin.site.register(MainComment)
admin.site.register(SubComment)