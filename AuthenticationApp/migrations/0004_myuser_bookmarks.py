# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0004_auto_20161207_1311'),
        ('AuthenticationApp', '0003_auto_20161207_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bookmarks',
            field=models.ManyToManyField(to='ProjectsApp.Project'),
        ),
    ]
