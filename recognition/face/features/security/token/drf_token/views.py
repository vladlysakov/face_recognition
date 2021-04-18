from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from face.common.security.decorators import admin_authentication
from face.features.security.token.drf_token.service import get_token


class ObtainExpiringAuthToken(ObtainAuthToken):
    @admin_authentication
    def post(self, request, user, *args, **kwargs):
        token: Token = get_token(user)

        return Response({'token': token.key})
