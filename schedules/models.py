from django.db import models
from experiments.models import Experiment


class Schedule(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    institution = models.CharField(max_length=255)
    date = models.DateField()
    time_init = models.TimeField()
    time_end = models.TimeField()
    number_users = models.IntegerField()
    register = models.CharField(max_length=15)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)