"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from ProjectsApp.forms import ProjectForm, ProjectUpdateForm
from ProjectsApp.models import Project
from . import models


def getProjects(request):
    projects_list = models.Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects_list,
        'canCreate': request.user.is_engineer or request.user.is_admin
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
def update_project(request):
    if request.user.is_engineer:
        project_name = request.GET.get('name', None)
        project = get_object_or_404(Project, name=project_name)
        form = ProjectUpdateForm(request.POST or None, instance=project)
        if form.is_valid():
            form.save()
            return getProject(request)
        return render(request, 'update_project.html', {'form': form, "button_value": "Update"})


@login_required
def getProjectForm(request):
    if request.user.is_engineer or request.user.is_admin:
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            if models.Project.objects.filter(name__exact=form.data['name']).exists():
                return messages.error(request, 'Name already exists!')
            project = Project(
                name=form.data['name'],
                description=form.data['description'],
                language=form.data['language'],
                experience=form.data['experience'],
                specialty=form.data['specialty']
            )
            project.save()
            return render(request, 'project.html', {'project': project})
        return render(request, 'update_project.html', {'form': form, "button_value": "Create"})
    else:
        return render(request, 'autherror.html', status=403)


@login_required
def deleteProject(request):
    if not (request.user.is_engineer or request.user.is_admin):
        return render(request, 'autherror.html')
    project_name = request.GET.get('name', 'None')
    project = get_object_or_404(Project, name=project_name)
    project.delete()
    return getProjects(request)
