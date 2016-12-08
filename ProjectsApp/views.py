"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from ProjectsApp.forms import ProjectForm
from ProjectsApp.models import Project
from . import models


def getProjects(request):
    projects_list = models.Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects_list,
        'canCreate': request.user.is_engineer
    })


def getProject(request):
    project_name = request.GET.get('name', None)
    project = get_object_or_404(Project, name=project_name)
    is_bookmarked = request.user.bookmarks.filter(name__exact=project_name)
    return render(request, 'project.html', {
        'project': project,
        'isBookmarked': is_bookmarked
    })


@login_required
def getProjectForm(request):
    if request.user.is_engineer:
        return render(request, 'projectform.html')
    else:
        return render(request, 'autherror.html', status=403)


@login_required
def getProjectFormSuccess(request):
    if not request.user.is_engineer:
        return render(request, 'autherror.html')
    form = ProjectForm(request.POST)
    if models.Project.objects.filter(name__exact=form.data['name']).exists():
        return render(request, 'projectform.html', {'error': 'Name already exists'})
    new_project = Project(
        name=form.data['name'],
        description=form.data['description'],
        language=form.data['language'],
        experience=form.data['experience'],
        specialty=form.data['specialty']
    )
    new_project.save()
    context = {
        'project': new_project
    }
    return render(request, 'project.html', context)


@login_required
def deleteProject(request):
    if not (request.user.is_engineer or request.user.is_admin):
        return render(request, 'autherror.html')
    project_name = request.GET.get('name', 'None')
    project = get_object_or_404(Project, name=project_name)
    project.delete()
    return getProjects(request)
