from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.translation import gettext as _
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    fullname = models.TextField(_("full name"),max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('fullname',)

    objects = UserManager()

    def __str__(self):
        return self.email
