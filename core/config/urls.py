"""
justshipto_core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('justshipto_core.core.urls')),
    path('accounts/', include('justshipto_core.accounts.urls')),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
