import graphene
from django.contrib.auth import get_user_model
from graphql import GraphQLError

from .types import UserType


class UserQueries:
    me = graphene.Field(UserType)
    profile = graphene.Field(UserType, id=graphene.Int())

    def resolve_me(self, info, **kwargs):
        return info.context.user

    def resolve_profile(self, info, **kwargs):
        try:
            return get_user_model().objects.get(**kwargs)
        except get_user_model().DoesNotExist:
            return GraphQLError('User does not exists')
