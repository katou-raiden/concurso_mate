from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    
    class Meta:
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
        ]
        model = User

#class StudentForm(forms.ModelForm):

  #  class Meta:
   #     fields = ['pui', 'grade']
  #      model = Student

#class ProfessorForm(forms.ModelForm):
#
 #   class Meta:
 #       fields = ['work_at', 'phone_number']
  #      model = Professor
