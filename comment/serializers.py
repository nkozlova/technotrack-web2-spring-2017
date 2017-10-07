from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')
    id = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'
