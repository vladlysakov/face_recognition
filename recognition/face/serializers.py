from face.features.recognition.service import create_user, create_recognition_data
from face.models import CustomUser, FaceRecognition
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = create_user(**validated_data)
        create_recognition_data(user=user)

        return user


class FaceRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceRecognition
        fields = '__all__'
