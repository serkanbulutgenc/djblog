from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.account.views import AccountLoginView, ProfileView

app_name = 'accounts'
urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
    ]
