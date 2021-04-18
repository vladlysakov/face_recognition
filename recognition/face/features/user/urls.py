from django.urls import path

from face.features.user.logic.views import Users, User, Authenticate

urlpatterns = [
    path('users', Users.as_view(), name='List of Users'),
    path('user', User.as_view(), name='Create user'),
    path('user/authenticate', Authenticate.as_view(), name='Authenticate user')
]
