# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import User, Post, Comment, Like
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer
from core.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
import json


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        return instance.save()


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


    def perform_destroy(self, instance):
        return instance.save()


class LikeViewSet(ModelViewSet):

    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        return instance.save()
