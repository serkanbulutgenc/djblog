from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.user.views import (
    AccountLoginView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    SignupView,
)

app_name = 'account'
urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
