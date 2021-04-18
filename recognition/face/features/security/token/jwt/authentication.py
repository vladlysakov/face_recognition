from rest_framework_simplejwt.views import TokenObtainPairView

from face.features.security.token.jwt.serializers import JWTAuthenticationSerializer


class JWTObtain(TokenObtainPairView):
    serializer_class = JWTAuthenticationSerializer
