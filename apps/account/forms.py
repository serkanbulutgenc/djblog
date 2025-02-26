from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AdminUserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
    UserChangeForm,
    UserCreationForm,
)


class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = get_user_model()
        # fields = AdminUserCreationForm.Meta.fields + ('phone',)
        # exclude = ('usable_password')


class CustomAdminUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # fields = AdminUserCreationForm.Meta.fields + ('phone',)
        # exclude = ('first_name', 'last_name')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserLoginForm(AuthenticationForm):
    pass


class SignupForm(BaseUserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = BaseUserCreationForm.Meta.fields + ('phone',)
        # field_classes={
        #    "username":forms.CharField
        # }
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

    def save(self, **cleaned_data):
        print(cleaned_data)
        return super().save(**cleaned_data)
