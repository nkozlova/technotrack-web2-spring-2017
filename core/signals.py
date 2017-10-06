from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Comment, Like
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=Like)
def increment_likes_count(instance, created=False, *args, **kwargs):

    if created:
        instance.object.likes_count += 1
        instance.object.save()


@receiver(post_save, sender=Comment)
def increment_comments_count(instance, created=False, *args, **kwargs):

    if created:
        instance.object.comments_count += 1
        instance.object.save()


@receiver(post_delete, sender=Like)
def decrement_likes_count(instance, *args, **kwargs):

    instance.object.likes_count -= 1
    instance.object.save()


@receiver(post_delete, sender=Comment)
def decrement_comments_count(instance, *args, **kwargs):

    instance.object.comments_count += 1
    instance.object.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):

    if created:
        Token.objects.create(user=instance)