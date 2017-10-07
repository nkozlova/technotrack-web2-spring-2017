from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Like
        fields = '__all__'