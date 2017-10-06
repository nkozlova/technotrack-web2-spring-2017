# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import User, Post, Comment, Like, Relationship
from rest_framework.authtoken.admin import TokenAdmin


class RelationshipInline(admin.StackedInline):

    model = Relationship
    fk_name = 'user_from'
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    inlines = [RelationshipInline,]


class LikesInline(GenericStackedInline):

    model = Like
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


class CommentsInline(GenericStackedInline):

    model = Comment
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    fields = ('author', 'text',)


class AbleAdmin(admin.ModelAdmin):

    inlines = LikesInline, CommentsInline,


@admin.register(Post)
class PostAdmin(AbleAdmin):

    readonly_fields = ('comments_count', 'likes_count',)


@admin.register(Comment)
class CommentAdmin(AbleAdmin):

    fields = ('author', 'text', 'comments_count', 'likes_count',)
    readonly_fields = ('comments_count', 'likes_count',)


TokenAdmin.raw_id_fields = ('user',)