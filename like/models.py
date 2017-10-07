from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.models import ModelWithDates, ModelWithAuthor, ModelWithGenericKey


class Like(ModelWithDates, ModelWithAuthor, ModelWithGenericKey):

    class Meta:
        unique_together = ('author', 'content_type', 'object_id')


class LikeAble(models.Model):

    likes = GenericRelation(Like, object_id_field='object_id', content_type_field='content_type')
    likes_count = models.IntegerField(default=0)

    class Meta:
        abstract = True