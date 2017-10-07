from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Like


@receiver(post_save, sender=Like)
def increment_likes_count(instance, created=False, *args, **kwargs):

    if created:
        instance.content_object.likes_count += 1
        instance.content_object.save()


@receiver(post_delete, sender=Like)
def decrement_likes_count(instance, *args, **kwargs):

    instance.content_object.likes_count -= 1
    instance.content_object.save()
