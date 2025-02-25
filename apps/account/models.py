from uuid import uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    FileExtensionValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return f'user_{instance.owner.id}/{uuid4()}.{ext}'


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


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'
        UNKNOWN = 'unknown'

    owner = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='profile', help_text=_('User')
    )
    first_name = models.CharField(
        _('First Name'),
        max_length=30,
        null=True,
        blank=True,
        help_text=_('First Name'),
        validators=[MaxLengthValidator(50), MinLengthValidator(3)],
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=50,
        null=True,
        blank=True,
        help_text=_('First Name'),
        validators=[MaxLengthValidator(50), MinLengthValidator(3)],
    )
    gender = models.CharField(
        _('Gender'),
        choices=Gender.choices,
        default=Gender.UNKNOWN,
        max_length=10,
        help_text=_('Gender'),
    )
    bio = models.TextField(
        _('Bio'),
        max_length=100,
        null=True,
        blank=True,
        validators=[MaxLengthValidator(1000)],
        help_text=_('Bio'),
    )
    profile_picture = models.FileField(
        _('Profile Picture'),
        upload_to=get_file_name,
        null=True,
        blank=True,
        help_text=_('Profile Picture'),
        validators=[FileExtensionValidator(('jpg', 'jpeg', 'png'))],
    )
    created_at = models.DateTimeField(auto_created=True, auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def pp(self):
        return self.profile_picture or None

    def __str__(self):
        return 'Profile'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'
