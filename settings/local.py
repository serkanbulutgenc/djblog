from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list)

INTERNAL_IPS = ['127.0.0.1']

DATABASES = {'default': env.db_url('SQLITE_URL', default='sqlite:///db.sqlite3')}

DATABASES['default']['ATOMIC_REQUESTS'] = True

CACHES = {'default': env.cache_url('CACHE_URL')}

STORAGES = {
    'default': {'BACKEND': 'django.core.files.storage.FilesystemStorage'},
    #'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

THIRD_PARTY_APPS += ('debug_toolbar', 'apps.home.apps.HomeConfig')

INSTALLED_APPS += THIRD_PARTY_APPS
