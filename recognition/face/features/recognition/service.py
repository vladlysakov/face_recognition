import json
from datetime import datetime
from typing import Dict, List

import face_recognition as auth_tools
import numpy as np
from face.common.exceptions import RecognitionDataException
from face.features.camera.service import get_face_from_camera
from face.features.recognition import repository
from face.models import CustomUser, FaceRecognition
from pydash import get, is_empty, head
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone


def face_recognition(user: CustomUser):
    user_data = get_recognition_data(user.pk)
    camera_data = get_face_from_camera()

    if authenticate_by_face(user_data, camera_data):
        return user

    raise PermissionDenied(detail=f'Face recognition failed. You are not {user.email}.')


def authenticate_by_face(user_data, camera_data) -> bool:
    if is_empty(user_data.data):
        raise

    is_authenticated: List[bool] = auth_tools.compare_faces([user_data.data], camera_data)

    if head(is_authenticated):
        return True


def get_recognition_data(user_id: int):
    user_data = repository.get_recognition_data(user_id)

    if not user_data:
        raise RecognitionDataException()

    return user_data


def create_recognition_data(user: CustomUser) -> FaceRecognition:
    recognition_data = get_face_from_camera()
    face = FaceRecognition(user=user, data=recognition_data.tolist(), last_recognition=timezone.now())
    face.save()

    return face


def create_user(**validated_data: Dict) -> CustomUser:
    password: str = get(validated_data, 'password')
    user = CustomUser(**validated_data)
    user.set_password(password)
    user.save()

    return user
