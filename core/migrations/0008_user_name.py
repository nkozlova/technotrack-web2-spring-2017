# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170917_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]