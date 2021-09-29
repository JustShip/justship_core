from django.contrib import admin

from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'get_full_name', 'is_superuser']
    list_filter = ['is_superuser']
    search_fields = ['username', 'first_name', 'last_name']
