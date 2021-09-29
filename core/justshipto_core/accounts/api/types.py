import graphene
from graphene_django import DjangoObjectType

from core.justshipto_core.accounts.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'is_active',
            'date_joined',
            'last_login'
        )


user_types = [
    UserType
]