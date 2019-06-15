from django.db import models


class Experiment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    domain = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads/exps', blank=True)

    class Meta:
        ordering = ('name',)
