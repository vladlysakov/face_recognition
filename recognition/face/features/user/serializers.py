from rest_framework.serializers import ModelSerializer

from face.features.user.logic import service
from face.features.user.repository.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser

        fields = [
            'id',
            'email',
            'last_login',
            'first_name',
            'last_name',
            'date_joined',
            'address',
            'birthday',
            'birthday',
            'phone_number',
            'student_id'
        ]

    def create(self, validated_data):
        user = service.create_user(validated_data)

        return user
