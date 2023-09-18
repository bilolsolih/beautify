from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'phone_number', 'email']
    list_display_links = ['id', 'username', 'phone_number', 'email']
    list_filter = ['is_active', 'is_verified']
    fieldsets = (
        (None, {'fields': ('phone_number', 'username', 'email', 'is_verified', 'is_active')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('phone_number', 'username', 'email', 'full_name', 'password1', 'password2')
            }
        ),
    )
    search_fields = ['full_name', 'username', 'phone_number', 'email']
    readonly_fields = ['last_login', 'created', 'updated']
    ordering = ('-created',)


admin.site.register(User, CustomUserAdmin)
