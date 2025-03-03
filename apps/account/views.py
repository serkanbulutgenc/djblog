from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from django.contrib.auth.views import PasswordResetCompleteView as BasePasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView as BasePasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView as BasePasswordResetDoneView
from django.contrib.auth.views import PasswordResetView as BasePassordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from apps.account.forms import (
    CustomUserLoginForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    SignupForm,
)


class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomUserLoginForm
    redirect_authenticated_user = True
    redirect_field_name = 'redirect'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class SignupView(SuccessMessageMixin, CreateView):
    form_class = SignupForm
    template_name = 'account/signup.html'
    success_url = reverse('index', urlconf='apps.home.urls')
    success_message = '%(username)s was created successfully'
    redirect_authenticated_users = True


class PasswordChangeView(SuccessMessageMixin, BasePasswordChangeView):
    template_name = 'account/password-change.html'
    form_class = PasswordChangeForm
    success_message = 'Password has been changed successfully'
    success_url = reverse('index', urlconf='apps.userprofile.urls')


class PasswordResetView(UserPassesTestMixin, BasePassordResetView):
    def test_func(self):
        return not self.request.user.is_authenticated

    template_name = 'account/password-reset-form.html'
    form_class = PasswordResetForm
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('core:account:password_reset_done')


class PasswordResetDoneView(BasePasswordResetDoneView):
    template_name = 'account/password-reset-done.html'


class PasswordResetConfirmView(BasePasswordResetConfirmView):
    """Presents a form for entering a new password."""

    template_name = 'account/password-reset-confirm.html'
    success_url = reverse_lazy('core:account:password_reset_complete')
    form_class = SetPasswordForm


class PasswordResetCompleteView(BasePasswordResetCompleteView):
    template_name = 'account/password-reset-complete.html'
