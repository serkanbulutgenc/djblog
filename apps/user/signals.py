import contextlib

from allauth.account.signals import user_logged_in, user_logged_out, user_signed_up
from django.contrib.auth import get_user_model
from django.db import OperationalError
from django.dispatch import receiver

from apps.userprofile.models import Profile


@receiver(user_signed_up, sender=get_user_model())
def create_profile(signal, sender, request, user, **kwargs):
    try:
        Profile.objects.create(owner=user)
    except OperationalError:
        contextlib.suppress(OperationalError)
        # TODO log profile creation or use try except


@receiver([user_logged_in, user_logged_out], sender=get_user_model())
def logged_in(signal, sender, request, user, **kwargs):
    print('user', signal, sender, request, user)
