import graphene

from justship.apps.accounts.api.types import UserType
from justship.apps.accounts.models import User


class UpdateUsername(graphene.Mutation):
    class Arguments:
        identifier = graphene.Int()
        username = graphene.String()
    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, identifier, username):
        current_user = info.context.user
        user = User.objects.get(pk=identifier)
        if user and (user == current_user or current_user.is_staff):
            user.username = username if username is not None else user.username
            user.save()
            return UpdateUsername(ok=True, user=user)
        return UpdateUsername(ok=False, user=None)


class UserMutations(graphene.ObjectType):
    update_username = UpdateUsername.Field()
