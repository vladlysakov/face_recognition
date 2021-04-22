from django.urls import path

from face.features.user.logic.views import Users, User, Authenticate

urlpatterns = [
    path('user', User.as_view(), name='Create user'),
    path('users', Users.as_view(), name='List of Users'),
    path('user/authenticate', Authenticate.as_view(), name='Authenticate user')
]
