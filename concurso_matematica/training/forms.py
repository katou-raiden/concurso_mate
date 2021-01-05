from django import forms
from .models import Completed_Exercise
from .models import Exercise,  Sugestion,Level,Topic
from .fields import GroupedModelChoiceField




class Completed_ExerciseForm(forms.Form):
    points = forms.TypedChoiceField(coerce=int, choices=list(zip(range(0,8), range(0,8))))
    def save(self, student, exercise):
        print(self.cleaned_data)
        Completed_Exercise.objects.create(points=self.cleaned_data.get('points'), student=student, exercise=exercise)

    
  
        
    
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
