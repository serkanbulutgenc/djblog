from django.urls import path, include 

app_name='core'
urlpatterns = [
    path('', include('apps.home.urls', namespace='home')),
    path('account/', include('apps.account.urls', namespace='account')),
    path('profile/', include('apps.userprofile.urls', namespace='userprofile')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard'))
]
