from rest_framework import serializers
from .models import User, UserToUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class SelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', )


class UserToUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserToUser
        fields = ('from_user', 'to_user')