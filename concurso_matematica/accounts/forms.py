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
            'email',
        ]
        model = User

class StudentForm(forms.ModelForm):

    class Meta:
        fields = ['pui', 'grade', 'private_number', 'phone_number', 'province']
        model = Student

class ProfessorForm(forms.ModelForm):

    class Meta:
        fields = ['institute', 'phone_number', 'private_number', 'province']
        model = Professor
