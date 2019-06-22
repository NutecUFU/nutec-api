from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


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

    def save(self, *args, **kwargs):
        self.is_active = False
        super().save(self, args, kwargs)

    class Meta:
        ordering = ('username',)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    lattes = models.URLField(blank=True, null=True, max_length=255)
    linked = models.URLField(blank=True, null=True, max_length=255)
    photo = models.ImageField(upload_to='uploads/users', default='http://nutec.ufu.br/assets/images/group/user.png')

