# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 09:14
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0004_auto_20161207_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(max_length=10000),
        ),
    ]
