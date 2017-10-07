from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from core.models import ModelWithDates, ModelWithAuthor, ModelWithGenericKey
from like.models import LikeAble


class Comment(ModelWithDates, ModelWithAuthor, ModelWithGenericKey, LikeAble):

    text = models.TextField()


class CommentAble(models.Model):

    comments = GenericRelation(Comment, object_id_field='object_id', content_type_field='content_type')
    comments_count = models.IntegerField(default=0)

    class Meta:
        abstract = True
