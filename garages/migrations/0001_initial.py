# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
            ],
        ),
    ]
