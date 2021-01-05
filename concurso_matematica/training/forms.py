from django import forms
from accounts.models import Completed_Exercise
from .models import Exercise,  Sugestion,Level,Topic
from .fields import GroupedModelChoiceField



class Completed_ExerciseForm(forms.ModelForm):

    
    class Meta:
        model = Completed_Exercise

        exclude = [
            'name'
        ]

class ExerciseForm(forms.ModelForm):
    
    topic = GroupedModelChoiceField(
        queryset=Topic.objects.exclude(level = None),
        choices_groupby = 'level'
    )
    class Meta:
        model = Exercise

        exclude = [
            'times_visited',
        ]

class SugestionForm(forms.ModelForm):

    class Meta:
        model = Sugestion

        exclude = [
            'exercise'
        ]
