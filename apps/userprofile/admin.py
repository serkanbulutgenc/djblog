from django.contrib import admin

from apps.userprofile.forms import ProfileForm
from apps.userprofile.models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['owner']
    empty_value_display = '-empty-'
    autocomplete_fields = ['owner']
    add_form = ProfileForm
