from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from face.common.security.decorators import token_authentication
from face.common.security.mixins import RecognitionAuthenticationMixin
from face.features.recognition.logic.service import create_or_update


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
