from django.db import models

class Schedule(models.Model):
    goal = models.CharField(max_length=500)
    stressors = models.CharField(max_length=500, blank=True)
    motivators = models.TextField(blank=True)

    def __str__(self):
        return self.goal

class Completed(models.Model):
    goal = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='completed')
    date = models.DateField(auto_now=True)

   
