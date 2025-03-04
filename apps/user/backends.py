from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

UserModel = get_user_model()


class EmailLoginBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        try:
            user = UserModel.objects.get(email=kwargs.get('username'))
        except UserModel.DoesNotExist:
            # TODO log error message
            return None
        else:
            if user and user.check_password(kwargs.get('password')):
                return user
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None


class PhoneLoginBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        try:
            user = UserModel.objects.get(phone=kwargs.get('username'))
        except UserModel.DoesNotExist:
            # TODO log error message
            return None
        else:
            if user and user.check_password(kwargs.get('password')):
                return user
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
