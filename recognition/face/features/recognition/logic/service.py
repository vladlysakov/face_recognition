import base64
import io
from datetime import datetime
from typing import List, Optional

import face_recognition as auth_tools
import numpy as np
from PIL import Image
from django.utils import timezone
from pydash import is_empty, head, get
from rest_framework.exceptions import PermissionDenied

from face.common.exceptions import RecognitionDataException
from face.features.camera.service import get_face_from_camera, encoding
from face.features.recognition.repository import repository
from face.features.recognition.repository.models import FaceRecognition
from face.features.user.repository.models import CustomUser


def face_recognition(user: CustomUser, data: str) -> CustomUser:
    user_data = get_recognition_data_verified(get(user, 'pk'))
    recognition_data = get_recognition_data_from_string(data)

    if authenticate_by_face(user_data.data, recognition_data):
        return user

    raise PermissionDenied(detail=f'Face recognition failed. You are not {user.email}.')


def authenticate_by_face(user_data, camera_data) -> bool:
    if is_empty(user_data):
        raise RecognitionDataException('Photo from camera has not been processed.')

    is_authenticated: List[bool] = auth_tools.compare_faces([user_data], camera_data)

    if head(is_authenticated):
        return True


def get_recognition_data_verified(user_id: int):
    user_data = repository.get_recognition_data(user_id)

    if not user_data:
        raise RecognitionDataException()

    return user_data


def create_recognition_data(user: CustomUser, time: datetime = None) -> FaceRecognition:
    time = time if time else timezone.now()

    recognition_data = get_face_from_camera()
    face = create(user=user, data=recognition_data.tolist(), last_recognition=time)
    repository.save(face)

    return face


def create(user: CustomUser, data, last_recognition: datetime = None) -> FaceRecognition:
    face = repository.create(user=user, data=data, last_recognition=last_recognition)

    return face


def create_or_update(serializer, user: CustomUser):
    recognition_instance = get(user, 'facerecognition')

    if not recognition_instance:
        face = create_recognition_data(user)
    else:
        face = get_face_from_camera()
        serializer = serializer(recognition_instance, data={'data': face.tolist()}, partial=True)

        if serializer.is_valid():
            serializer.save()

    return face


def verify_and_save_recognition_data(user: CustomUser, data: Optional[str] = None, time: datetime = None):
    time = time if time else timezone.now()
    recognition_data = get_recognition_data_from_string(data)

    if recognition_data:
        raise RecognitionDataException()

    face = create(user=user, data=recognition_data.tolist(), last_recognition=time)
    repository.save(face)

    return face


def get_recognition_data_from_string(recognition_data: str):
    type_, value = recognition_data.split(',')
    base64_decoded = base64.b64decode(value)

    with io.BytesIO(base64_decoded) as chunk:
        with Image.open(chunk) as image:
            arr = np.array(image)

    data = encoding(arr)

    return data
