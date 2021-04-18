from rest_framework.serializers import ModelSerializer

from face.features.recognition.repository.models import FaceRecognition


class FaceRecognitionSerializer(ModelSerializer):
    class Meta:
        model = FaceRecognition
        fields = '__all__'
