from abc import ABC, abstractmethod

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from face.features.security.token.drf_token.authentication import ExpiringTokenAuthentication
from face.models import CustomUser, FaceRecognition
from face.serializers import UserSerializer, FaceRecognitionSerializer


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
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class RecognitionAuthenticationMixin(AuthenticationMixin):
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = FaceRecognitionSerializer
    queryset = FaceRecognition.objects.all()
