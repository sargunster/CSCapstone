# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0002_auto_20161114_2200'),
        ('GroupsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProjectsApp.Project'),
        ),
    ]
