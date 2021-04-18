import os

from face.common.constants import DatabaseVariables


class DatabaseConfig:
    ENGINE = os.getenv(DatabaseVariables.ENGINE_NAME, DatabaseVariables.ENGINE)
    NAME = os.getenv(DatabaseVariables.TABLE_NAME, DatabaseVariables.NAME)
    USER = os.getenv(DatabaseVariables.USER_NAME, DatabaseVariables.USER)
    PASSWORD = os.getenv(DatabaseVariables.PASSWORD_NAME, DatabaseVariables.PASSWORD)
    HOST = os.getenv(DatabaseVariables.HOST_NAME, DatabaseVariables.HOST)
    PORT = os.getenv(DatabaseVariables.PORT_NAME, DatabaseVariables.PORT)

    AUTH_USER_MODEL = os.getenv(DatabaseVariables.AUTH_USER_MODEL_NAME, DatabaseVariables.AUTH_USER_MODEL)
