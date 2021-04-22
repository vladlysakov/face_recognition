from django.contrib.auth import authenticate
from pydash import get
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from face.common.security.decorators import token_authentication
from face.common.security.mixins import UserAuthenticationMixin
from face.features.recognition.logic import service as recognition_services
from face.features.user.serializers import UserSerializer, PostUserSerializer


class Users(UserAuthenticationMixin, ListAPIView):
    @token_authentication
    def get(self, request, user, *args, **kwargs):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)

        return Response({'users': serializer.data}, status=HTTP_200_OK)


class Authenticate(UserAuthenticationMixin, CreateAPIView):
    serializer_class = PostUserSerializer

    @token_authentication
    def post(self, request, admin, *args, **kwargs):
        user = authenticate(**get(request, 'data.user'))
        recognition_services.face_recognition(user, get(request, 'data.data'))
        serialized_user = UserSerializer(user)

        return Response({'users': serialized_user.data}, status=HTTP_200_OK)


class User(UserAuthenticationMixin, CreateAPIView):
    serializer_class = PostUserSerializer
