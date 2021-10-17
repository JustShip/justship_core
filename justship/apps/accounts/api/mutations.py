import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphql_jwt.utils import jwt_payload, jwt_encode
from graphql_jwt.signals import token_issued
from django.contrib.auth import get_user_model
from django.db.models import Q
from graphql import GraphQLError

from .types import UserType
from ..models import Follow
from justship.apps.mails.tasks import send_password_recovery_mail
from justship.apps.products import models as product_models
from justship.apps.resources import models as resources_models


class TokenAuth(graphene.Mutation):
    """
    Login user
    """
    ok = graphene.Boolean()
    token = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        User = get_user_model()

        try:
            if str(username).__contains__('@'):
                user = User.objects.get(email__iexact=username)
            else:
                user = User.objects.get(username__iexact=username)

            if user.check_password(raw_password=password) and user.is_active:
                # Response without first_login
                payload = jwt_payload(user)
                token = jwt_encode(payload)

                token_issued.send(
                    sender='TokenAuth',
                    request=info.context,
                    user=user
                )

                return TokenAuth(ok=True, token=token, user=user)

        except User.DoesNotExist:
            pass

        return TokenAuth(ok=False, user=None)


class SignUp(graphene.Mutation):
    """
    Register user
    """
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

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
    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()

    @staticmethod
    @login_required
    def mutate(root, info, username):
        user = info.context.user
        user.username = username if username is not None else user.username
        user.save()
        return UpdateUsername(ok=True, user=user)


class PasswordReset(graphene.Mutation):
    """
    Send a recovery password email
    """
    ok = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    @staticmethod
    def mutate(root, info, email):
        try:
            user = get_user_model().objects.get(email=email)
            temporal_code = user.generate_temporal_code()
            user.save()
            send_password_recovery_mail.delay(user.email, temporal_code)
        except get_user_model().DoesNotExist:
            return GraphQLError('Used does not exists')
        return PasswordReset(ok=True)


class PasswordResetConfirm(graphene.Mutation):
    """
    Request password reset
    """
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        temporal_code = graphene.String()
        password = graphene.String()

    @staticmethod
    def mutate(root, info, email, temporal_code, password):
        User = get_user_model()
        try:
            user = User.objects.get(email=email, temporal_code=temporal_code)
            # TODO: check password strength
            user.set_password(password)
            user.save()
            return PasswordResetConfirm(user=user)
        except User.DoesNotExist:
            return GraphQLError('Wrong code')


class ChangePassword(graphene.Mutation):
    """
    Change password
    """
    ok = graphene.Boolean()

    class Arguments:
        password = graphene.String()
        new_password = graphene.String()

    @staticmethod
    def mutate(root, info, password, new_password):
        user = info.context.user
        if not user.is_anonymous:
            if user.check_password(password):
                user.set_password(new_password)
                user.save()
                # TODO: get a new token and return it
                return ChangePassword(ok=True)
            else:
                return GraphQLError('Wrong password')
        return ChangePassword(ok=False)


class FollowUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        user_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, user_id):
        user = info.context.user

        # user not follow him/her self
        if user.pk == user_id:
            return GraphQLError('You can not follow yourself')

        to_follow = get_user_model().objects.filter(pk=user_id).first()

        # user to follow must exists
        if to_follow:
            # check if already exists
            follow, created = Follow.objects.get_or_create(follower=user, followed=to_follow)
            return FollowUser(ok=created)
        else:
            return GraphQLError('Wrong user id')


class UnfollowUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        user_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, user_id):
        user = info.context.user

        # you must not unfollow yourself
        if user.pk == user_id:
            return GraphQLError('You can not unfollow yourself')

        to_unfollow = get_user_model().objects.filter(pk=user_id).first()

        # check if user exists
        if to_unfollow:
            # check if you follow
            unfollow = Follow.objects.filter(Q(followed_id=user_id) & Q(follower=user)).first()
            unfollow.delete()
            return UnfollowUser(ok=True)
        else:
            return GraphQLError('Wrong user id')


class FollowProduct(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        product_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, product_id):
        """
        Add a product to an user's 'followed_products' attribute
        :param root:
        :param info:
        :param product_id: Product's id
        :return: Confirmation if follow was done successfully
        """
        user = info.context.user
        product = product_models.Product.objects.get(pk=product_id)

        if product:
            user.followed_products.add(product)
            user.save()
            return FollowProduct(ok=True)
        else:
            return GraphQLError('Error following a product')


class UnfollowProduct(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        product_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, product_id):
        """
        Remove a product from an user's 'followed_products' attribute
        :param root:
        :param info:
        :param product_id: Product's id
        :return: Confirmation if unfollow was done successfully
        """
        user = info.context.user
        product = product_models.Product.objects.get(pk=product_id)
        if product:
            user.followed_products.remove(product)
            user.save()
            return UnfollowProduct(ok=True)
        else:
            return GraphQLError('Error unfollowing a product')


class SaveResource(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        resource_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, resource_id):
        """
        Add a resource to an user 'saved_resources' field
        """
        user = info.context.user
        resource = resources_models.Resource.objects.get(pk=resource_id)

        if resource not in user.saved_resources.all():
            user.saved_resources.add(resource)
            user.save
            return SaveResource(ok=True)
        else:
            return GraphQLError("Already saved")


class DeleteSavedResource(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        resource_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, resource_id):
        """
        Remove a resource from an user 'saved_resources' field
        """
        user = info.context.user
        resource = resources_models.Resource.objects.get(pk=resource_id)

        if resource in user.saved_resources.all():
            user.saved_resources.remove(resource)
            user.save
            return DeleteSavedResource(ok=True)
        else:
            return GraphQLError("Resource doesn't exists on user saved_resources list ")


class UserMutations(graphene.ObjectType):
    # authenticate the User with its username or email and password to obtain the JSON Web token.
    token_auth = TokenAuth.Field()

    # confirm that the token is valid, passing it as an argument.
    verify_token = graphql_jwt.Verify.Field()

    # obtain a new token within the renewed expiration time for non-expired tokens, if they are enabled to expire.
    refresh_token = graphql_jwt.Refresh.Field()

    sign_up = SignUp.Field()
    update_username = UpdateUsername.Field()
    password_reset = PasswordReset.Field()
    password_reset_confirm = PasswordResetConfirm.Field()
    change_password = ChangePassword.Field()
    follow = FollowUser.Field()
    unfollow = UnfollowUser.Field()
    follow_product = FollowProduct.Field()
    unfollow_product = UnfollowProduct.Field()
    save_resource = SaveResource.Field()
    delete_saved_resource = DeleteSavedResource.Field()