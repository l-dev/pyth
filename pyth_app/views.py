from django.shortcuts import render, redirect
from .models import Schedule, Completed
from .forms import ScheduleForm

def schedule_list(request):
    schedule = Schedule.objects.all()
    return render(request, 'pyth/schedule_list.html', {'schedule' : schedule})
def completed_list(request):
    completed = Completed.objects.all()
    return render(request, 'pyth/completed_list.html', {'completed': completed})
def schedule_detail(request, pk):
    schedule = Schedule.objects.get(id=pk)
    return render(request, 'pyth/schedule_detail.html', {'schedule': schedule})
def completed_detail(request, pk):
    completed = Completed.objects.all()
    return render(request, 'pyth/completed_detail.html', {'completed':completed})
# def schedule_create(request):

# Create your views here.
