from pydash import get
from rest_framework.exceptions import AuthenticationFailed

from face.features.user.logic import service
from face.features.user.repository.models import CustomUser


def get_user(token):
    pk = get(token, 'payload.user_id')

    try:
        user = service.get_user(pk)
    except CustomUser.DoesNotExist:
        raise AuthenticationFailed('User with provided id does not exist.')

    return user
