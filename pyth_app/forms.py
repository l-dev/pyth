from django import forms
from .models import Schedule, Completed

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('goal', 'stressors', 'motivators')
