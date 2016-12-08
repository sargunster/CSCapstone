"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.shortcuts import render

from ProjectsApp.models import Project
from AuthenticationApp.models import MyUser


def getIndex(request):
    return render(request, 'index.html')


def getTable(request):
    return render(request, 'table.html')


def getForm(request):
    return render(request, 'form.html')


def handler404(request):
    return render(request, 'notfound.html', status=404)
