from django.urls import path

from face.features.recognition.logic.views import UserRecognition

urlpatterns = [
    path('user/recognition', UserRecognition.as_view(), name='Recognition user')
]
