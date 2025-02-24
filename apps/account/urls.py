from django.contrib.auth.views import LoginView
from django.urls import path

app_name = 'account'
urlpatterns = [path('login/', LoginView.as_view(template_name='account/login.html'), name='login')]
