# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 07:05
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0002_myuser_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='about',
            field=tinymce.models.HTMLField(default='Nothing here :('),
        ),
    ]
