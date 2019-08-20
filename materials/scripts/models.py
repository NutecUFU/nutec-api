from django.db import models


class Scripts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/materials/scripts')

    class Meta:
        ordering = ('name',)
