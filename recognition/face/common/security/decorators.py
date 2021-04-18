import functools

from pydash import get
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from face.features.security.utils import get_user, is_superuser
from face.models import CustomUser


# todo
def admin_authentication(method):
    """
    This decorator is working only for class-based views.
    """

    @functools.wraps(method)
    def decorated(self, request, *args, **kwargs):
        serializer_class = get(self, 'serializer_class')
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            user: CustomUser = get(serializer, 'validated_data.user')

            is_superuser(user)

            result = method(self, request, user, *args, **kwargs)

            return result
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return decorated


# todo
def token_authentication(method):
    @functools.wraps(method)
    def decorated(self, request, *args, **kwargs):
        token: Token = get(request, 'auth')

        user: CustomUser = get_user(token)
        is_superuser(user)

        result = method(self, request, user, *args, **kwargs)

        return result

    return decorated
