from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ModelWithAuthor(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)

    class Meta:
        abstract = True


class ModelWithDates(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ModelWithGenericKey(models.Model):

    object_id = models.PositiveIntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
