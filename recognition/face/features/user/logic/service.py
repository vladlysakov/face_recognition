from typing import Dict

from django.db import transaction
from pydash import get

from face.features.recognition.logic.service import create_recognition_data
from face.features.user.repository import repository
from face.features.user.repository.models import CustomUser
from face.features.user.repository.repository import save


def create_user_object(user_data: Dict) -> CustomUser:
    password: str = get(user_data, 'password')
    user = CustomUser(**user_data)
    user.set_password(password)
    save(user)

    return user


def create_user(user_data: Dict):
    with transaction.atomic():
        user = create_user_object(user_data)
        create_recognition_data(user=user)

    return user


def get_user(pk: int):
    user = repository.get_user(pk)

    return user
