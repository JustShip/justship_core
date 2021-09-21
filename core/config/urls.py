"""
justshipto_core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('justshipto_core.core.urls')),
    path('accounts/', include('justshipto_core.accounts.urls')),
]
