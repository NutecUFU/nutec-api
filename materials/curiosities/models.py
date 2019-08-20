from django.db import models


class Curiosities(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/materials/curiosities')

    class Meta:
        ordering = ('name',)
