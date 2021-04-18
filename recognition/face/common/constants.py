from datetime import timedelta


class EnvironmentVariables:
    DEFAULT_RETRIES_LIMIT = 3


class TokenVariables:
    ACCESS_TOKEN_LIFETIME = timedelta(seconds=3600)


class JWTTokenVariables(TokenVariables):
    REFRESH_TOKEN_LIFETIME = timedelta(days=1)
    SLIDING_TOKEN_LIFETIME = timedelta(minutes=30)
    SLIDING_TOKEN_REFRESH_LIFETIME = timedelta(days=1)
    AUTH_HEADER_NAME = 'HTTP_AUTHORIZATION'
    USER_ID_FIELD = 'id'
    USER_ID_CLAIM = 'user_id'
    AUTH_HEADER_TYPES = ('Bearer',)
    AUTH_TOKEN_CLASSES = ('rest_framework_simplejwt.tokens.AccessToken',)
    TOKEN_TYPE_CLAIM = 'token_type'
    JTI_CLAIM = 'jti'
    SLIDING_TOKEN_REFRESH_EXP_CLAIM = 'refresh_exp'
    ALGORITHM = 'HS256'


class KeysVariables:
    SECRET_KEY = 'SECRET_KEY'
    SECRET_KEY_VALUE = 'h*qbjz(^7$k%1syw8pts^kjw7q82$n8hc6%)xo8efh0_ccmwy_'


class AllowedHostsVariables:
    DEFAULT_HOST_NUMBER = '0.0.0.0'
    DEFAULT_HOST_NAME = 'localhost'

    ALL = [DEFAULT_HOST_NUMBER, DEFAULT_HOST_NAME]


class DatabaseVariables:
    ENGINE_NAME = 'ENGINE'
    ENGINE = 'django.db.backends.postgresql'

    HOST_NAME = 'HOST'
    HOST = 'localhost'

    PORT_NAME = 'PORT'
    PORT = 5432

    TABLE_NAME = 'NAME'
    NAME = 'face_recognition'

    USER_NAME = 'DATABASE_USER'
    USER = 'postgres'

    PASSWORD_NAME = 'PASSWORD'
    PASSWORD = '1'

    AUTH_USER_MODEL_NAME = 'AUTH_USER_MODEL'
    AUTH_USER_MODEL = 'face.CustomUser'


class ErrorHandlersVariables:
    HANDLER500 = 'handler500'
    HANDLER400 = 'handler400'

    HANDLER500_VALUE = 'rest_framework.exceptions.server_error'
    HANDLER400_VALUE = 'rest_framework.exceptions.bad_request'
