from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(_('email address'))
    message = models.TextField()
