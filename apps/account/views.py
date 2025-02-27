from django.contrib.auth.views import LoginView
from apps.account.forms import CustomUserLoginForm
from django.views.generic import FormView,CreateView
from apps.account.forms import SignupForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomUserLoginForm
    redirect_authenticated_user=True
    redirect_field_name='redirect'

class SignupView(SuccessMessageMixin,CreateView):
    form_class = SignupForm
    template_name='account/signup.html'
    success_url=reverse('index',urlconf='apps.home.urls')
    success_message = "%(username)s was created successfully"
    
