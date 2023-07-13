from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account
from .forms import AccountCreationForm, AccountChangeForm


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'birth_date', 'is_superuser', 'is_staff',
                    'is_active', 'role', 'modified_date', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    list_filter = ('created_date', 'is_superuser', 'is_staff', 'is_active', 'role')
    date_hierarchy = 'created_date'
    ordering = ()
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date', 'avatar')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'role',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('modified_date', 'created_date')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2'), }),
    )
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(Account, AccountAdmin)
