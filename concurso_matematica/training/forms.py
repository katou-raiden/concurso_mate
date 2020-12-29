from django import forms
from accounts.models import Completed_Exercise


class Completed_ExerciseForm(forms.ModelForm):
    class Meta:
        model = Completed_Exercise

        exclude = [
            'name'
        ]