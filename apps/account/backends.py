from django.contrib.auth.backends import BaseBackend

class EmailLoginBackend(BaseBackend):
    
    def authenticate(self, request, **kwargs):
        print(kwargs)
        return super().authenticate(request, **kwargs)
    
    def get_user(self, user_id):
        return super().get_user(user_id)
    
class PhoneLoginBackend(BaseBackend):
    
    def authenticate(self, request, **kwargs):
        print(kwargs)
        return super().authenticate(request, **kwargs)
    
    def get_user(self, user_id):
        return super().get_user(user_id)