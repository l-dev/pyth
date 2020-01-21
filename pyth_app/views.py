from django.shortcuts import render
from .models import Schedule, Completed

def schedule_list(request):
    goals = Schedule.objects.all()
    return render(request, 'pyth_app/goals_list.html', {'goals' : goals})
def completed_list(request):
    completed = Completed.objects.all()
    return render(request, 'pyth_app/completed_list.html', {'comppleted': completed})
# Create your views here.
