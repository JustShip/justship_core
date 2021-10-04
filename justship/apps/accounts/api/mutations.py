import graphene
from django.contrib.auth import get_user_model
from django.db.models import Q
from graphql import GraphQLError

from .types import UserType
from .. import utils
from ..models import Follow
from ...mails.tasks import send_recovery_mail


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

    class Arguments:
        email = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, email):
        domain = info.context.headers['Origin']
        try:
            user = get_user_model().objects.get(email=email)
            uid = utils.generate_uid(user.pk)
            token = utils.generate_token(user)
            send_recovery_mail.delay(user.email, domain, uid, token)
        except get_user_model().DoesNotExist:
            return GraphQLError('no existe un usuario con ese email')
        return PasswordReset(ok=True)


class PasswordResetConfirm(graphene.Mutation):
    """
    Change user password
    """

    class Arguments:
        uid = graphene.String()
        token = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, uid, token, password):
        pk = utils.decode_uid(uid)
        try:
            user = get_user_model().objects.get(pk=pk)
            if utils.is_correct_token(user, token):
                # TODO: check password strength
                user.set_password(password)
                user.save()
                return PasswordResetConfirm(user=user)
            else:
                return GraphQLError('token incorrecto')
        except get_user_model().DoesNotExist:
            return GraphQLError('uid incorrecto')


class ChangePassword(graphene.Mutation):
    class Arguments:
        password = graphene.String()
        new_password = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, password, new_password):
        user = info.context.user
        if not user.is_anonymous:
            is_correct_password = user.check_password(password)
            if is_correct_password:
                user.set_password(new_password)
                user.save()
                # TODO: get a new token and return it
                return ChangePassword(ok=True)
            else:
                return GraphQLError('contraseña incorrecta')
        return ChangePassword(ok=False)


class FollowUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()

    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, user_id):
        user = info.context.user

        # user must be logged
        if user.is_authenticated:
            # user not follow him/her self
            if user.pk == user_id:
                return GraphQLError('No puedes seguirte a ti mismo')

            to_follow = get_user_model().objects.filter(pk=user_id).first()

            # user to follow must exists
            if to_follow:
                # check if already exists
                follow, is_created = Follow.objects.get_or_create(follower=user, followed=to_follow)
                return FollowUser(status=is_created)
            else:
                return GraphQLError('Id del usuario no válido')
        else:
            return GraphQLError('Debes estar autenticado')


class UnfollowUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()

    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, user_id):
        user = info.context.user

        # user must be logged
        if user.is_authenticated:
            # you must not unfollow yourself
            if user.pk == user_id:
                return GraphQLError('No puedes dejar de seguirte a ti mismo')

            to_unfollow = get_user_model().objects.filter(pk=user_id).first()
            # check if user exists
            if to_unfollow:
                # check if you follow
                unfollow = Follow.objects.filter(Q(followed_id=user_id) & Q(follower=user)).first()
                unfollow.delete()
                return UnfollowUser(status=True)
            else:
                return GraphQLError('Id del usuario no válido')
        else:
            return GraphQLError('Debes estar autenticado')


class UserMutations(graphene.ObjectType):
    sign_up = SignUp.Field()
    update_username = UpdateUsername.Field()
    password_reset = PasswordReset.Field()
    password_reset_confirm = PasswordResetConfirm.Field()
    change_password = ChangePassword.Field()
    follow = FollowUser.Field()
    unfollow = UnfollowUser.Field()
