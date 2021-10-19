from graphene_django import DjangoObjectType

from justship.apps.accounts.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'onboarding_completed',
            'verified',
            'patreon',
            'team',
            'avatar_url',
            'avatar_thumbnail_url',
            'cover_url',
            'cover_thumbnail_url',
            'follows',
            'is_active',
            'date_joined',
            'last_login',
            'followed_products',
            'saved_resources'

        )


user_types = [
    UserType
]
