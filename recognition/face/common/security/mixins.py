from abc import ABC, abstractmethod

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from face.features.recognition.serializers import FaceRecognitionSerializer
from face.features.security.token.drf.authentication import TokenAuthentication
from face.features.user.serializers import UserSerializer
from face.models import CustomUser, FaceRecognition


class AuthenticationMixin(ABC):

    @property
    @abstractmethod
    def authentication_classes(self):
        pass

    @property
    @abstractmethod
    def permission_classes(self):
        pass

    @property
    @abstractmethod
    def serializer_class(self):
        pass

    @property
    @abstractmethod
    def queryset(self):
        pass


class UserAuthenticationMixin(AuthenticationMixin):
    authentication_classes = (JWTTokenUserAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class RecognitionAuthenticationMixin(AuthenticationMixin):
    authentication_classes = (JWTTokenUserAuthentication, TokenAuthentication,)
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = FaceRecognitionSerializer
    queryset = FaceRecognition.objects.all()
