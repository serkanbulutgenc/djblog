import contextlib

from django.contrib.auth import get_user_model
from django.db import OperationalError
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.account.models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created and isinstance(instance, get_user_model()):
        try:
            Profile.objects.create(owner=instance)
        except OperationalError:
            contextlib.suppress(OperationalError)
        # TODO log profile creation or use try except
