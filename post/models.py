from django.db import models
from core.models import ModelWithAuthor, ModelWithDates
from like.models import LikeAble
from comment.models import CommentAble


class Post(ModelWithDates, ModelWithAuthor, LikeAble, CommentAble):

    title = models.CharField(max_length=255, default='')
    text = models.TextField()
