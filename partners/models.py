from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='uploads/partners')
    link = models.CharField(max_length=255)
