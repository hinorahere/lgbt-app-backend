from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .managers import CustomUserManager
from profiles.models import Profile


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    matches = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='+',
                                     blank=True)

    prospects = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='+',
                                       blank=True)

    rejects = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='+',
                                     blank=True)
    def __str__(self):
        return str(self.pk)
