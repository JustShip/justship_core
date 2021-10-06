from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name']
    search_fields = ['name', 'description']


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    fields = ['url', 'category', 'image', 'description', 'creator']
    list_display = ['url', 'description', 'creator']
    search_fields = ['url', 'description']
