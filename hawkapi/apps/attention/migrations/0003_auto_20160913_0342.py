# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attention', '0002_auto_20160907_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='attention',
            name='details',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='attention',
            name='report_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attention',
            name='uid',
            field=models.IntegerField(default=0),
        ),
    ]