from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import Comment
from .serializers import CommentSerializer
from core.permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(CommentViewSet, self).get_queryset()
        if self.request.query_params.get('object_id') and self.request.query_params.get('content_type'):
            qs = qs.filter(object_id=self.request.query_params.get('object_id'),
                    content_type=self.request.query_params.get('content_type'))
        return qs