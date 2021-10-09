from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name']
    search_fields = ['name', 'description']


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    fields = ['url', 'title', 'category', 'image', 'description', 'creator']
    list_display = ['title', 'url', 'description', 'creator']
    search_fields = ['title', 'url', 'description']
