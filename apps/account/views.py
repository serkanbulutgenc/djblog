from django.contrib.auth.views import LoginView
from apps.account.forms import CustomUserLoginForm
from django.views.generic import FormView
from apps.account.forms import SignupForm
from django.urls import reverse

class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomUserLoginForm
    redirect_authenticated_user=True
    redirect_field_name='redirect'

class SignupView(FormView):
    form_class = SignupForm
    template_name='account/signup.html'
    success_url=reverse('index',urlconf='apps.home.urls')
    
