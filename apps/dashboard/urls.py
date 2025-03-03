from django.urls import path

from apps.dashboard.views import DashboardView, ProfileView

app_name = 'dashboard'
urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
