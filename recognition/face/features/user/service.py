from typing import Dict

from pydash import get

from face.features.user.repository import save
from face.models import CustomUser


def create_user(**validated_data: Dict) -> CustomUser:
    password: str = get(validated_data, 'password')
    user = CustomUser(**validated_data)
    user.set_password(password)
    save(user)

    return user
