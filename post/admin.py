from django.contrib import admin

from .models import Post
from like.admin import LikeAbleAdmin
from comment.admin import CommentAbleAdmin


@admin.register(Post)
class PostAdmin(LikeAbleAdmin, CommentAbleAdmin):

    fields = ('author', 'title', 'text', 'comments_count', 'likes_count',)
    readonly_fields = ('comments_count', 'likes_count',)
    inlines = LikeAbleAdmin.inlines + CommentAbleAdmin.inlines
