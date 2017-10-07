from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Comment


@receiver(post_save, sender=Comment)
def increment_comments_count(instance, created=False, *args, **kwargs):

    if created:
        instance.content_object.comments_count += 1
        instance.content_object.save()


@receiver(post_delete, sender=Comment)
def decrement_comments_count(instance, *args, **kwargs):

    instance.content_object.comments_count -= 1
    instance.content_object.save()