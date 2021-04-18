from django.urls import path

from face.features.security.token.drf_token.views import ObtainExpiringAuthToken
from face.views import *

urlpatterns = [
    path('users', Users.as_view(), name='List of Users'),
    path('user', User.as_view(), name='Create user'),
    path('user/authenticate', Authenticate.as_view(), name='Authenticate user'),
    path('user/recognition', UserRecognition.as_view(), name='Recognition user'),
    path('user/auth/token', ObtainExpiringAuthToken.as_view(), name='Obtain access token')
]
