from datetime import datetime
from typing import Tuple

from rest_framework.authtoken.models import Token

from face.features.user.repository.models import CustomUser


def get_token(key: str) -> Token:
    token: Token = Token.objects.get(key=key)

    return token


def get_or_create(user: CustomUser) -> Tuple[Token, bool]:
    token, created = Token.objects.get_or_create(user=user)

    return token, created


def delete(token: Token) -> None:
    token.delete()


def generate_token(user: CustomUser) -> Token:
    token: Token = Token.objects.create(user=user)

    return token


def update(token: Token, time: datetime) -> None:
    token.created = time
    token.save()
