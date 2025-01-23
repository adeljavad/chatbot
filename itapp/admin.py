1
from django.contrib import admin
# from django.contrib.auth.models import Group, User
# from django.contrib.auth.admin import UserAdmin, GroupAdmin
# from .models import (
#     AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser,
#     AuthUserGroups, AuthUserUserPermissions, DjangoAdminLog,
#     DjangoContentType, DjangoMigrations, DjangoSession
# )

# ثبت مدل‌های پیش‌فرض
# admin.site.register(User, UserAdmin)
# admin.site.register(Group, GroupAdmin)

# # ثبت مدل‌های دیگر
# admin.site.register(AuthGroup)
# admin.site.register(AuthGroupPermissions)
# admin.site.register(AuthPermission)
# admin.site.register(AuthUser)
# admin.site.register(AuthUserGroups)
# admin.site.register(AuthUserUserPermissions)
# admin.site.register(DjangoAdminLog)
# admin.site.register(DjangoContentType)
# admin.site.register(DjangoMigrations)
# admin.site.register(DjangoSession)

# سفارشی‌سازی نمایش AuthUser
# class AuthUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('username', 'email')
#     list_filter = ('is_staff', 'is_active')

# admin.site.register(AuthUser, AuthUserAdmin)