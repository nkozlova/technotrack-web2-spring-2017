# -*- config: utf8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Post, User, Comment, Like


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'is_staff')


class PostSerializer(ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Like
        fields = '__all__'
