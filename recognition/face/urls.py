from django.urls import path

from face.views import *

urlpatterns = [
    path('users', Users.as_view(), name='user-list'),
    path('user', User.as_view(), name='create-user'),
    path('user/authenticate', Authenticate.as_view(), name='authenticate-user'),
    path('user/recognition', UserRecognition.as_view(), name='recognition-user')
]
