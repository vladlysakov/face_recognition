from django.contrib.postgres.fields import ArrayField
from django.db import models

from face.features.user.repository.models import CustomUser


class FaceRecognition(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, default=None)
    last_recognition = models.DateTimeField(default=None, verbose_name='last_success_recognition')
    data = ArrayField(models.FloatField(), default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user.name}'
