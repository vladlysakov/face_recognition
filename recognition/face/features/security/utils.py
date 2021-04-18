from datetime import timedelta

from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from face.common.constants import TokenVariables
from face.features.security.token.drf import service as drf_service
from face.features.security.token.jwt import service as jwt_service
from face.features.user.repository.models import CustomUser


def validate_token(token):
    if not token.user.is_active:
        raise AuthenticationFailed("The User inactive or deleted.")

    is_expired = is_token_expired(token)

    if is_expired:
        raise AuthenticationFailed("The Access token has expired.")


def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = TokenVariables.ACCESS_TOKEN_LIFETIME - time_elapsed

    return left_time


def is_token_expired(token):
    return expires_in(token) < timedelta(seconds=0)


def is_superuser(user: CustomUser):
    if not user:
        raise AuthenticationFailed()
    elif not user.is_superuser:
        raise PermissionDenied("Only admins can initiate auth flow.")


def get_user(token):
    user = drf_service.get_user(token)

    if not user:
        user = jwt_service.get_user(token)

    return user
