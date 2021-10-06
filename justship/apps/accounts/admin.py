from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'get_full_name', 'is_superuser']
    list_filter = ['is_superuser']
    search_fields = ['username', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('Otros datos', {'fields': ('creator_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Otros datos', {'fields': ('creator_type',)}),
    )


@admin.register(models.Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'followed', 'created_at', 'is_recent']
    list_filter = ['followed__first_name']
    search_fields = ['created_at', 'follower', 'followed']


# Remove Group from Django admin
admin.site.unregister(Group)
