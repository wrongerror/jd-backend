# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_checkthree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkthree',
            name='search',
            field=models.CharField(max_length=256),
        ),
    ]
