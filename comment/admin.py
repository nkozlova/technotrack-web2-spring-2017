from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Comment
from like.admin import LikeAbleAdmin


@admin.register(Comment)
class CommentAdmin(LikeAbleAdmin):

    pass


class CommentsInline(GenericStackedInline):

    model = Comment
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    fields = ('author', 'text',)


class CommentAbleAdmin(admin.ModelAdmin):

    inlines = [CommentsInline, ]
    readonly_fields = ['comments_count', 'likes_count']
