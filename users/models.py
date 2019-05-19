from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserManager(AbstractUserManager):
    pass


class User(AbstractUser):
    objects = UserManager()
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email) 


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    lattes = models.URLField(blank=True, null=True, max_length=255)
    linked = models.URLField(blank=True, null=True, max_length=255)
    photo = models.ImageField(upload_to='uploads', default='http://nutec.ufu.br/assets/images/group/user.png')
