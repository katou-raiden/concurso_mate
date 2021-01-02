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
        fields = ['pui', 'grade']
        model = Student
    
    

class ProfessorForm(forms.ModelForm):

    class Meta:
        fields = ['institute']
        model = Professor
        widgets = {
            'institute' : forms.TextInput,
        }
   
class ProfileForm(forms.ModelForm):
    
    class Meta:
        fields = '__all__'
        exclude = ['user']
        model = Profile
        

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field, forms.CharField):
                field.widget = forms.TextInput(attrs={'class': 'form-control'})
            elif not isinstance(field, forms.ImageField):
                field.attrs.update({'class': 'form-control'})
            
