import graphene
from django.contrib.auth import get_user_model

from justship.apps.accounts.api.types import UserType


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
        user = get_user_model()(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return SignUp(user=user)


class UserMutations(graphene.ObjectType):
    sign_up = SignUp.Field()
