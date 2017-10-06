# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):

    name = models.CharField(max_length=255)
    objects_count = models.IntegerField(default=0)
    signers = models.ManyToManyField(to='self', through='Relationship', symmetrical=False,
                                     related_name='related_to')


class Relationship(models.Model):

    user_from = models.ForeignKey(User, related_name='users_from')
    user_to = models.ForeignKey(User, related_name='users_to')



class ModelWithDates(models.Model):

    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования', auto_now=True)

    class Meta:
        abstract = True


class ModelWithAuthor(models.Model):

    author = models.ForeignKey(User, verbose_name='Пользователь')

    class Meta:
        abstract = True



class WithGenericKey(models.Model):

    object_id = models.PositiveIntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class Like(ModelWithAuthor, ModelWithDates, WithGenericKey):

    class Meta:
        unique_together = ('author', 'content_type', 'object_id')


class LikeAble(models.Model):

    likes = GenericRelation(Like, object_id_field='object_id', content_type_field='content_type')
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Comm(ModelWithAuthor, ModelWithDates, LikeAble, WithGenericKey):

    pass


class CommentAble(models.Model):

    comments = GenericRelation(Comm, object_id_field='object_id', content_type_field='content_type')
    comments_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Comment(ModelWithAuthor, ModelWithDates, LikeAble, CommentAble, WithGenericKey):

    text = models.TextField('Сообщение', default='')


class Post(ModelWithAuthor, ModelWithDates, LikeAble, CommentAble):

    title = models.CharField('Тема', max_length=255)
    text = models.TextField('Описание', default='')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
