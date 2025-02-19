from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list)

DATABASES = {
    'default': env.db(),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

CACHES = {
    # read os.environ['REDIS_URL']
    'default': env.cache_url('REDIS_URL')
}

THIRD_PARTY_APPS += ('apps.home.apps.HomeConfig',)

INSTALLED_APPS += THIRD_PARTY_APPS
