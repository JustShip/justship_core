import graphene

from .types import UserType


class UserQueries:
    me = graphene.Field(UserType)

    def resolve_me(self, info, **kwargs):
        return info.context.user
