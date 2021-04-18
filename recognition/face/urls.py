from face.features.recognition.urls import urlpatterns as recognition_urls
from face.features.security.token.drf.urls import urlpatterns as drf_token_urls
from face.features.security.token.jwt.urls import urlpatterns as jwt_token_urls
from face.features.user.urls import urlpatterns as user_urls

urlpatterns = []

urlpatterns.extend(user_urls)
urlpatterns.extend(recognition_urls)
urlpatterns.extend(drf_token_urls)
urlpatterns.extend(jwt_token_urls)
