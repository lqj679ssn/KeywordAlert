# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0008_auto_20170703_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='group_id',
            field=models.IntegerField(default=None, verbose_name='GROUP ID'),
        ),
    ]
