from face.decorators import custom_authenticate
from face.features.camera.service import get_face_from_camera
from face.features.recognition import service
from face.features.recognition.service import create_recognition_data
from face.models import CustomUser, FaceRecognition
from face.serializers import UserSerializer, FaceRecognitionSerializer
from pydash import get
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class Users(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)

        return Response({'users': serializer.data}, status=status.HTTP_200_OK)


class Authenticate(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    @custom_authenticate
    def post(self, request, *args, **kwargs):
        user = get(kwargs, 'user')

        service.face_recognition(user)
        serialized_user = UserSerializer(user)

        return Response({'users': serialized_user.data}, status=status.HTTP_200_OK)


class User(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserRecognition(UpdateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = FaceRecognitionSerializer
    queryset = FaceRecognition.objects.all()

    @custom_authenticate
    def update(self, request, *args, **kwargs):
        user = get(kwargs, 'user')
        recognition_instance = get(user, 'facerecognition')

        if not recognition_instance:
            create_recognition_data(user)
        else:
            face = get_face_from_camera()
            serializer = self.get_serializer(recognition_instance, data={'data': face.tolist()}, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response({'message': 'Face recognition data have been updated successfully'})

        return Response(
            {'message': f'Face recognition updating has benn failed.'}, status=status.HTTP_400_BAD_REQUEST)
