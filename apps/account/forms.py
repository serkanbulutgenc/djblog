from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AdminUserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
    UserChangeForm,
)
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm
from django.utils.translation import gettext as _


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


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login-form'
        self.helper.form_class = 'loginForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Login',
                FloatingField('username', wrapper_class='wrapper-class'),
                FloatingField('password'),
                Div(),
                Div(
                    Submit('submit', 'Login', css_class='btn-block'),
                    css_id='form-actions-area',
                    css_class='d-grid gap-2',
                ),
            )
        )

    # class Meta:
    # super().__init__().Meta()
    # widgets = {"username":forms.TextInput(attrs={"class":'form-control', "placeholder":'username or email'})}


class SignupForm(BaseUserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, help_text=None, label=_('password'))
    is_read = forms.BooleanField(
        required=True,
        label='I agree terms & conditions',
        error_messages={'required': _('You should accept term and conditions before signup.')},
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-signup-form'
        self.helper.form_class = 'signupForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Signup',
                FloatingField('username'),
                FloatingField('phone'),
                FloatingField('password1'),
                FloatingField('password2'),
                Div(Field('is_read')),
                Div(
                    Submit('submit', 'Signup', css_class='btn-block'),
                    css_id='form-actions-area',
                    css_class='d-grid gap-2',
                ),
            )
        )

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = BaseUserCreationForm.Meta.fields + ('phone', 'is_read')
        # field_classes={
        #    "username":forms.CharField
        # }
        # widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'}) }

    def save(self, commit=True):
        print('c : ---- : ', self.cleaned_data)
        user = super().save(commit=False)
        user.phone = self.cleaned_data.get('phone', None)
        user.save()
        return user


class PasswordChangeForm(BasePasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'password-change-form'
        self.helper.layout = Layout(
            Fieldset(
                'Change Password',
                'old_password',
                'new_password1',
                'new_password2',
                Field(Submit('submit', 'Change')),
            )
        )
