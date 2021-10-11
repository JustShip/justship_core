from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name']
    search_fields = ['name', 'description']


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
    fields = ['url', 'categories', 'image', 'description', 'creator']
    list_display = ['url', 'description', 'creator']
    search_fields = ['url', 'description']


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    fields = ['resource', 'voted_by']
    list_display = ['resource', 'voted_by']
    search_fields = ['resource', 'voted_by']