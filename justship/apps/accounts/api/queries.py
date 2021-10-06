import graphene
from django.contrib.auth import get_user_model
from graphql import GraphQLError

from .types import UserType


class UserQueries:
    me = graphene.Field(UserType)
    profile = graphene.Field(UserType, username=graphene.String())

    def resolve_me(self, info, **kwargs):
        return info.context.user

    def resolve_profile(self, info, username):
        """
        Given the username, returns the user. If this isn't exists throw error
        :param info: request and metadata info
        :param username: username to search
        :return: if user exists returns, else throw error
        """
        try:
            return get_user_model().objects.get(username__iexact=username)
        except get_user_model().DoesNotExist:
            return GraphQLError('User does not exists')
