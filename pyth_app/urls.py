from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('completed/', views.completed_list, name='completed_list'),
    path('schedule/<int:pk>', views.schedule_detail, name='schedule_detail'),
    path('completed/<int:pk>', views.completed_detail, name='completed_detail'),
    path('schedule/new', views.schedule_create, name='schedule_create'),

]