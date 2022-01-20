from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = ['id',
                  'username',
                  'email',
                  'password',
                  'prospects',]

        validators = [
            UniqueTogetherValidator(
                queryset=CustomUser.objects.all(),
                fields=['username', 'email']
            )
        ]
