from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def generate_uid(pk: int) -> str:
    """
    Generate a unique uid from user id
    :param pk: User id
    :return: User id encode in base64
    """
    return urlsafe_base64_encode(force_bytes(pk))


def generate_token(user: get_user_model()) -> str:
    """
    Return a token that can be used once to do a password reset
    for the given user. Set PASSWORD_RESET_TIMEOUT in settings for
    life time
    :param user: User object
    :return: A hash token
    """
    return default_token_generator.make_token(user)


def decode_uid(uid: str) -> str:
    """
    Decode a base64 encoded string. Add back any trailing equal signs that
    might have been stripped.
    :param uid:
    :return:
    """
    return urlsafe_base64_decode(uid)


def is_correct_token(user: get_user_model(), token: str) -> bool:
    """
    Check that a password reset token is correct for a given user.
    :param user: the user for change password
    :param token: the token for change password
    :return: True if token is correct for the given user
    """
    return default_token_generator.check_token(user, token)
