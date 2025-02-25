# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.account.forms import CustomAdminUserChangeForm, CustomAdminUserCreationForm
from apps.account.models import Profile


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'phone')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'phone'),
            },
        ),
    )
    add_form = CustomAdminUserCreationForm
    form = CustomAdminUserChangeForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'owner__username']
    empty_value_display = '-empty-'
