from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminUserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomAdminUserCreationForm(AdminUserCreationForm):

    class Meta(AdminUserCreationForm.Meta):
        model=get_user_model()
        #fields = AdminUserCreationForm.Meta.fields + ('phone',)
        #exclude = ('usable_password')
        
class CustomAdminUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model=get_user_model()
        #fields = AdminUserCreationForm.Meta.fields + ('phone',)
        #exclude = ('first_name', 'last_name')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserLoginForm(AuthenticationForm):
    pass
        