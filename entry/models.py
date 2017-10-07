from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from core.models import ModelWithDates


class Entry(ModelWithDates):

    text = models.CharField(max_length=300)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_type = models.IntegerField()
