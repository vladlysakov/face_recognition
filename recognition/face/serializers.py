from rest_framework.serializers import ModelSerializer

from face.features.recognition.service import create_recognition_data
from face.features.user.service import create_user
from face.models import CustomUser, FaceRecognition


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser

        fields = [
            'id',
            'email',
            'last_login',
            'first_name',
            'last_name',
            'date_joined',
            'address',
            'birthday',
            'birthday',
            'phone_number',
            'student_id'
        ]

    def create(self, validated_data):
        user = create_user(**validated_data)
        create_recognition_data(user=user)

        return user


class FaceRecognitionSerializer(ModelSerializer):
    class Meta:
        model = FaceRecognition
        fields = '__all__'
