from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from face.features.security.token.jwt.authentication import JWTObtain

urlpatterns = [
    path('auth/jwt_token/obtain', JWTObtain.as_view(), name='token_obtain_pair'),
    path('auth/jwt_token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/jwt_token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
