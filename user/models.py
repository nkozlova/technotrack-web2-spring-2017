from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation

from copy import deepcopy


class User(AbstractUser):

    objects_count = models.IntegerField(default=0)
    follows = models.ManyToManyField('self', symmetrical=False,
                                     through='UserToUser', through_fields=('from_user', 'to_user'),
                                     related_name='followed_by'
                                     )


class UserToUser(models.Model):

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')

    class Meta:
        unique_together = ('from_user', 'to_user')
