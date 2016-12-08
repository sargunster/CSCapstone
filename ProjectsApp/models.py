"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from django.utils.datetime_safe import datetime
import tinymce.models


class Project(models.Model):
    name = models.CharField(unique=True, max_length=200)
    description = tinymce.models.HTMLField(max_length=10000)
    created_at = models.DateTimeField('date created', default=datetime.now)
    updated_at = models.DateTimeField('date updated', default=datetime.now)
    language = models.CharField(max_length=200, null=True)
    experience = models.IntegerField(null=True)
    specialty = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name