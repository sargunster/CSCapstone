# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0004_myuser_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='qualifications',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='specification',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]