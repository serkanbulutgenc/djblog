from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None 
    phone=models.CharField(_("phone_number"), max_length=10)


    USERNAME_FIELD='username'
    EMAIL_FIELD=['email']
    REQUIRED_FIELDS=['email']




