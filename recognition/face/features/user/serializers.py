from rest_framework import serializers
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
            'student_id',
            'password'
        ]

        extra_kwargs = {'password': {'write_only': True}}


class PostUserSerializer(serializers.Serializer):
    user = UserSerializer()
    data = serializers.CharField(max_length=300000, min_length=2, allow_blank=False, required=True)

    def create(self, validated_data):
        user = service.create_user(validated_data)

        return user

    def update(self, instance, validated_data):
        super(PostUserSerializer, self).update(instance, validated_data)

    def to_representation(self, obj):
        response = super(PostUserSerializer, self).to_representation(obj)
        response.pop('data')

        return response
