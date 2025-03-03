# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.account.forms import CustomAdminUserChangeForm, CustomAdminUserCreationForm
from apps.userprofile.models import Profile


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    @admin.display(description=_('Is Verified?'), boolean=True)
    def is_verified(self, instance):
        return instance.profile.is_verified

    list_display = ('username', 'email', 'is_staff', 'is_verified', 'last_login')
    fieldsets = (
        (
            _('General Information'),
            {'classes': ['wide'], 'fields': ('username', 'password', 'phone')},
        ),
        (
            _('Attributes'),
            {
                'classes': ['collapse'],
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
        (
            _('Gropus and Permission'),
            {
                'classes': ['collapse'],
                'fields': (
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
                'fields': ('username', 'email', 'phone', 'password1', 'password2'),
            },
        ),
    )
    add_form = CustomAdminUserCreationForm
    form = CustomAdminUserChangeForm
    actions_selection_counter = True
    list_filter = ('is_active', 'is_staff')
    date_hierarchy = 'last_login'
    list_select_related = ('profile',)
    show_facets = admin.ShowFacets.ALLOW
    # filter_vertical=['groups', 'user_permissions']
    # list_editable=('is_staff',)
    search_fields = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'owner']
    empty_value_display = '-empty-'
    autocomplete_fields = ['owner']
