from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Fieldset, Layout, Row, Submit
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AdminUserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
    UserChangeForm,
)
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.contrib.auth.forms import SetPasswordForm as BaseSetPasswordForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = get_user_model()
        fields = AdminUserCreationForm.Meta.fields + ('email',)
        # exclude = ('usable_password')


class CustomAdminUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # fields = AdminUserCreationForm.Meta.fields + ('phone',)
        # exclude = ('first_name', 'last_name')


class CustomUserLoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput,max_length=30, label=None, help_text=None)
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login-form'
        self.helper.form_class = 'loginForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                None,
                PrependedText('username', '@', placeholder='username', wrapper_class=None),
                PrependedText('password', '@', placeholder='password', wrapper_class=None),
                Row(
                    Div(Submit('submit', 'Login', css_class='px-4'), css_class='col-6'),
                    Div(
                        HTML(
                            f'<a href="{reverse_lazy("core:account:password_reset")}" class="btn btn-link px-0">Forgot Password</a>'
                        ),
                        css_class='col-6 text-end',
                    ),
                    css_id='form-actions-area',
                ),
            )
        )

    # class Meta:
    #    fields=('username', 'password')
    # super().__init__().Meta()
    # widgets = {"username":forms.TextInput(attrs={"class":'form-control', "placeholder":'username or email'})}


class SignupForm(BaseUserCreationForm):
    username = forms.CharField(label=None)
    password1 = forms.CharField(widget=forms.PasswordInput, help_text=None, label=_('password'))
    password2 = None
    email = forms.EmailField(
        widget=forms.EmailInput, required=True, help_text=None, label=_('Email')
    )
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
                None,
                PrependedText('username', '@', css_class='form-control-sm'),
                PrependedText('email', '@', css_class='form-control-sm'),
                PrependedText('password1', '*', css_class='form-control-sm'),
                Div(Field('is_read')),
                Row(
                    Submit('submit', 'Signup', css_class='btn-block btn-success'),
                    css_id='form-actions-area',
                    css_class='d-grid gap-2',
                ),
            )
        )

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = BaseUserCreationForm.Meta.fields + ('email', 'is_read')
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
                Div(
                    Submit('submit', 'Login', css_class='btn-block'),
                    css_id='form-actions-area',
                    css_class='d-grid gap-2',
                ),
            )
        )


class PasswordResetForm(BasePasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'password-reset-form'
        self.helper.form_id = 'password-reset-form-id'
        self.helper.layout = Layout(
            Fieldset(
                None,
                'email',
                Div(
                    Submit('submit', 'Send', css_class='btn-block'),
                    css_id='form-actions-area',
                    css_class='d-grid gap-2',
                ),
            )
        )


class SetPasswordForm(BaseSetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'password-reset-form-class'
        self.helper.form_id = 'password-reset-form-id'
        self.helper.layout = Layout(
            'Reset Password',
            'new_password1',
            'new_password2',
            Div(Submit('submit', 'Set Password'), css_class='btn btn-primary'),
        )
