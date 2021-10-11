from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'link', 'state']
    list_display = ['name', 'description', 'link', 'state']
    search_fields = ['name']
