# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 08:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170916_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
