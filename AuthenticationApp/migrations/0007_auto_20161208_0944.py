# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0006_auto_20161208_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_admin',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_engineer',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_professor',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_student',
            field=models.NullBooleanField(default=False),
        ),
    ]
