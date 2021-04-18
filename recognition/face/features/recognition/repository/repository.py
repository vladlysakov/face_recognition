from datetime import datetime
from typing import Dict

from face.features.recognition.repository.models import FaceRecognition
from face.features.user.repository.models import CustomUser


def get_recognition_data(user_id: int):
    data = FaceRecognition.objects.filter(user=user_id)

    return data.first()


def save(face: FaceRecognition) -> None:
    face.save()


def create(user: CustomUser, data: Dict, last_recognition: datetime) -> FaceRecognition:
    face = FaceRecognition(user=user, data=data, last_recognition=last_recognition)

    return face
