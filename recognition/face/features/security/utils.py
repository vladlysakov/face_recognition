from datetime import timedelta

from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from face.common.constants import TokenVariables
from face.models import CustomUser


def validate_token(token):
    if not token.user.is_active:
        raise AuthenticationFailed("The User inactive or deleted.")

    is_expired = is_token_expired(token)

    if is_expired:
        raise AuthenticationFailed("The Access token has expired.")


def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=TokenVariables.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    return left_time


def is_token_expired(token):
    return expires_in(token) < timedelta(seconds=0)


def is_superuser(user: CustomUser):
    if not user:
        raise AuthenticationFailed()

    elif not user.is_superuser:
        raise PermissionDenied("Only admins can initiate auth flow.")
