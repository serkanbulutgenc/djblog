from django.apps import AppConfig

# from django.db.models.signals import post_save
# from apps.account.signals import create_profile


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        pass

        # Explicitly connect a signal handler.
        # post_save.connect(create_profile)
