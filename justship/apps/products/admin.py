from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'link', 'state', 'owner']
    list_display = ['name', 'description', 'link', 'state', 'owner']
    search_fields = ['name', 'owner']
