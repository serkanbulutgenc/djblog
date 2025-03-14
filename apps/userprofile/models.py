from uuid import uuid4

from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return f'user_{instance.owner.id}/{uuid4()}.{ext}'
# Create your models here.

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
    is_verified=models.BooleanField('Is Verified?', default=False, help_text=_('Verified status'), editable=False, blank=True)
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

