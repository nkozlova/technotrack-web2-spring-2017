from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'
