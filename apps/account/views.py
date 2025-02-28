from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView

from apps.account.forms import CustomUserLoginForm, PasswordChangeForm, SignupForm


class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomUserLoginForm
    redirect_authenticated_user = True
    redirect_field_name = 'redirect'
    extra_context = {'foo': 'bar'}

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
