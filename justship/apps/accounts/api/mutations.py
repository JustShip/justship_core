import graphene
from django.contrib.auth import get_user_model

from .types import UserType


class SignUp(graphene.Mutation):
    """
    Register user
    """

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, username, email, password):
        if info.context.user.is_anonymous:
            user = get_user_model()(
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()

            return SignUp(user=user)
        return SignUp(user=None)


class UpdateUsername(graphene.Mutation):
    """
    Update current user's username
    """

    class Arguments:
        username = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, username):
        user = info.context.user
        if not user.is_anonymous:
            user.username = username if username is not None else user.username
            user.save()
            return UpdateUsername(ok=True, user=user)
        return UpdateUsername(ok=False, user=None)


class PasswordReset(graphene.Mutation):
    """
    Send a recovery password email
    """


class PasswordResetConfirm(graphene.Mutation):
    """
    Change user password
    """


class UserMutations(graphene.ObjectType):
    sign_up = SignUp.Field()
    update_username = UpdateUsername.Field()
