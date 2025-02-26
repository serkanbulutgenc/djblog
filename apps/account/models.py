
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    FileExtensionValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, UserManager

# Create your models here.

class CustomUserManager(UserManager):
    def create_user(self, username, email = ..., password = ..., **extra_fields):
        print(username, email, password, extra_fields)
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    first_name = None
    last_name = None
    phone = models.CharField(
        _('Phone Number'),
        max_length=10,
        blank=True,
        null=True,
        help_text=_('Phone Number'),
        validators=[MinLengthValidator(7), MaxLengthValidator(10)],
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = ['email']
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return f'{self.username}'
