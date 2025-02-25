# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.account.forms import CustomAdminUserChangeForm,CustomAdminUserCreationForm
from django.utils.translation import gettext_lazy as _


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    list_display=("username","email", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password", "phone")}),
       
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        )
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "phone"),
            },
        ),
    )
    add_form=CustomAdminUserCreationForm
    form=CustomAdminUserChangeForm

    
