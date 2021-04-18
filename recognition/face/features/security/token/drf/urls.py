from django.urls import path

from face.features.security.token.drf.views import ObtainExpiringAuthToken

urlpatterns = [
    path('user/auth/token', ObtainExpiringAuthToken.as_view(), name='Obtain access token')
]
