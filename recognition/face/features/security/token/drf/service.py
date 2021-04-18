from datetime import datetime

from pydash import get
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from face.features.security.token.drf import repository
from face.features.security.utils import is_token_expired
from face.features.user.repository.models import CustomUser


def get_token(user: CustomUser) -> Token:
    token, created = Token.objects.get_or_create(user=user)

    if not created:
        token: Token = recreate(token)

    return token


def get_token_verified(key) -> Token:
    try:
        return repository.get_token(key)
    except Token.DoesNotExist:
        raise AuthenticationFailed("The Access token is invalid.")


def delete(token: Token) -> None:
    repository.delete(token)


def generate_token(user: CustomUser) -> Token:
    token = repository.generate_token(user)

    return token


def update(token: Token) -> None:
    time = datetime.utcnow()
    repository.update(token, time)


def regenerate(token: Token) -> Token:
    delete(token)
    token: Token = generate_token(token.user)

    return token


def recreate(token: Token) -> Token:
    if is_token_expired(token):
        token: Token = regenerate(token)
    else:
        update(token)

    return token


def get_user(token: Token) -> CustomUser:
    return get(token, 'user')
