from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from face.common.security.decorators import token_authentication
from face.common.security.mixins import UserAuthenticationMixin, RecognitionAuthenticationMixin
from face.features.recognition import service
from face.features.recognition.service import create_or_update
from face.serializers import UserSerializer


class Users(UserAuthenticationMixin, ListAPIView):
    @token_authentication
    def get(self, request, user, *args, **kwargs):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)

        return Response({'users': serializer.data}, status=HTTP_200_OK)


class Authenticate(UserAuthenticationMixin, CreateAPIView):
    @token_authentication
    def post(self, request, user, *args, **kwargs):
        service.face_recognition(user)
        serialized_user = UserSerializer(user)

        return Response({'users': serialized_user.data}, status=HTTP_200_OK)


class User(CreateAPIView, UserAuthenticationMixin):
    pass


class UserRecognition(UpdateAPIView, RecognitionAuthenticationMixin):
    @token_authentication
    def update(self, request, user, *args, **kwargs):
        serializer = self.get_serializer()
        face = create_or_update(serializer=serializer, user=user)

        if face:
            return Response({'message': 'Face recognition data have been updated successfully'}, status=HTTP_200_OK)

        return Response(
            {'message': f'Face recognition updating has benn failed.'},
            status=HTTP_400_BAD_REQUEST
        )
