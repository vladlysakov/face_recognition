import os

from face.common.constants import KeysVariables


class SecretKeyConfig:
    KEY = os.getenv(KeysVariables.SECRET_KEY, KeysVariables.SECRET_KEY_VALUE)
