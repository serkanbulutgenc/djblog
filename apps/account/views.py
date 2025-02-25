from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.account.forms import CustomUserLoginForm

class AccountLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomUserLoginForm
    redirect_authenticated_user=True
    redirect_field_name='redirect'

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "account/profile.html"

    
