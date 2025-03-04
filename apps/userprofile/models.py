from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return f'user_{instance.owner.id}/{uuid4()}.{ext}'


# Create your models here.


class Profile(models.Model):
    owner = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='profile', help_text=_('User')
    )
    info = models.JSONField(
        _('Information'), help_text=_('User information'), default=None, blank=True, null=True
    )
    is_verified = models.BooleanField(
        'Is Verified?', default=False, help_text=_('Verified status'), editable=False, blank=True
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
