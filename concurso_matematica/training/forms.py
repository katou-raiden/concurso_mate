from django import forms
from accounts.models import Completed_Exercises


class Completed_ExerciseForm(forms.ModelForm):
    class Meta:
        model = Completed_Exercises

        exclude = [
            'name'
        ]