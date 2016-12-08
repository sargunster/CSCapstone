"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from uuid import uuid4

from django.db import models
from AuthenticationApp.models import MyUser

# Create your models here.
from ProjectsApp.models import Project


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
    project = models.ForeignKey(Project, null=True)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    time = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(MyUser)
    group = models.ForeignKey(Group)

