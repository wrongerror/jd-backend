# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('unicode', models.CharField(max_length=32)),
                ('data', models.TextField()),
                ('swift_number', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unicode', models.CharField(max_length=32)),
                ('report_id', models.IntegerField()),
                ('idcard', models.CharField(max_length=20)),
                ('cell', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=11)),
                ('mail', models.CharField(max_length=32)),
                ('bank_id', models.CharField(max_length=32)),
                ('flag', models.CharField(max_length=32)),
                ('metadata', models.TextField()),
                ('formateddata', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('expire_in', models.IntegerField(default='7200')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
