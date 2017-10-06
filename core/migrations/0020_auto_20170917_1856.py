# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_comment_comments_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
    ]
