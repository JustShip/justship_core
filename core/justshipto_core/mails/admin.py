from django.contrib import admin
from django.utils.html import mark_safe

from . import models


@admin.register(models.EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    fields = ('sender', 'to', 'subject', 'html')
    list_display = ('sender', 'to', 'subject', 'created_at', '_get_html')
    readonly_fields = ('sender', 'to', 'subject', 'html', 'created_at', 'updated_at')
    search_fields = ('email',)

    def _get_html(self, obj):
        return mark_safe(obj.html)
