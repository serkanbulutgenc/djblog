from django.urls import path 
from apps.userprofile.views import ProfileView
app_name = 'userprofile'
urlpatterns = [
    path('',ProfileView.as_view(), name='index' )
]
