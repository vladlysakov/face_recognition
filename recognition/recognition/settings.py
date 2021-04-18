from pathlib import Path

from face.common.constants import JWTTokenVariables, AllowedHostsVariables
from face.configurations.database import DatabaseConfig
from face.configurations.keys import SecretKeyConfig

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SecretKeyConfig.KEY

DEBUG = True

ALLOWED_HOSTS = AllowedHostsVariables.ALL
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
    'face'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recognition.urls'

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'face.serializers.UserSerializer',
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'face.features.security.token.drf.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',)
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': JWTTokenVariables.ACCESS_TOKEN_LIFETIME,
    'REFRESH_TOKEN_LIFETIME': JWTTokenVariables.REFRESH_TOKEN_LIFETIME,
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': JWTTokenVariables.ALGORITHM,
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': JWTTokenVariables.AUTH_HEADER_TYPES,
    'AUTH_HEADER_NAME': JWTTokenVariables.AUTH_HEADER_NAME,
    'USER_ID_FIELD': JWTTokenVariables.USER_ID_FIELD,
    'USER_ID_CLAIM': JWTTokenVariables.USER_ID_CLAIM,

    'AUTH_TOKEN_CLASSES': JWTTokenVariables.AUTH_TOKEN_CLASSES,
    'TOKEN_TYPE_CLAIM': JWTTokenVariables.TOKEN_TYPE_CLAIM,

    'JTI_CLAIM': JWTTokenVariables.JTI_CLAIM,

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': JWTTokenVariables.SLIDING_TOKEN_REFRESH_EXP_CLAIM,
    'SLIDING_TOKEN_LIFETIME': JWTTokenVariables.SLIDING_TOKEN_LIFETIME,
    'SLIDING_TOKEN_REFRESH_LIFETIME': JWTTokenVariables.SLIDING_TOKEN_REFRESH_LIFETIME,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'recognition.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': DatabaseConfig.ENGINE,
        'NAME': DatabaseConfig.NAME,
        'USER': DatabaseConfig.USER,
        'PASSWORD': DatabaseConfig.PASSWORD,
        'HOST': DatabaseConfig.HOST,
        'PORT': DatabaseConfig.PORT,
    }
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
AUTH_USER_MODEL = DatabaseConfig.AUTH_USER_MODEL

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
