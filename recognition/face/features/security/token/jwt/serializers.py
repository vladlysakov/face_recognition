from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JWTAuthenticationSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        super(JWTAuthenticationSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        super(JWTAuthenticationSerializer, self).create(validated_data)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token
