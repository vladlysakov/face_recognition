from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from face.features.security.token.drf_token.service import get_token_verified
from face.features.security.utils import validate_token


class ExpiringTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        token: Token = get_token_verified(key)
        validate_token(token)

        return token.user, token
