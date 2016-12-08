"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from GroupsApp.forms import MemberForm
from GroupsApp.models import Group, Comment
from . import models
from . import forms


def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups': groups_list,
            'isStudent': request.user.is_student
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = get_object_or_404(Group, name=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        context = {
            'group': in_group,
            'userIsMember': is_member,
            'comments': models.Comment.objects.filter(group=in_group),
            'project': in_group.project
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def getGroupForm(request):
    if request.user.is_authenticated() and request.user.is_student:
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def getGroupFormSuccess(request):
    if request.user.is_authenticated() and request.user.is_student:
        if request.method == 'POST':
            form = forms.GroupForm(request.POST)
            if form.is_valid():
                if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'groupform.html', {'error': 'Error: That Group name already exists!'})
                new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                new_group.save()
                new_group.members.add(request.user)
                new_group.save()
                request.user.group_set.add(new_group)
                request.user.save()
                context = {
                    'name': form.cleaned_data['name'],
                }
                return render(request, 'groupformsuccess.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


@login_required
def deleteGroup(request):
    in_group_name = request.GET.get('name', 'None')
    in_group = get_object_or_404(Group, name=in_group_name)
    if in_group.members.filter(email__exact=request.user.email).exists():
        in_group.delete()
    return getGroups(request)


@login_required
def addToGroup(request):
    in_group_name = request.GET.get('name', 'None')
    in_group = get_object_or_404(Group, name=in_group_name)
    if in_group.members.filter(email__exact=request.user.email).exists():
        form = MemberForm(request.POST)
        new_member = models.MyUser.objects.get(email__exact=form.data['email'])
        new_member.group_set.add(in_group)
        new_member.save()
        in_group.members.add(new_member)
        in_group.save()
        return getGroup(request)
    return render(request, 'autherror.html')


@login_required
def linkToProject(request):
    in_group_name = request.GET.get('name', 'None')
    in_group = get_object_or_404(Group, name=in_group_name)
    if in_group.members.filter(email__exact=request.user.email).exists():
        return render(request, 'linkform.html', {'group': in_group})
    return render(request, 'autherror.html')


@login_required
def getLinkFormSuccess(request):
    if request.method == 'POST':
        form = forms.GroupForm(request.POST)
        in_group_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.filter(name__exact=in_group_name).first()
        if in_group is None:
            return render(request, 'notfound.html', status=404)
        project = models.Project.objects.filter(name__exact=form.data['name']).first()
        if project is None:
            return render(request, 'linkform.html', {'error': 'Project does not exist'})
        in_group.project = project
        in_group.save()
        return getGroup(request)
    return render(request, 'autherror.html')


@login_required
def addComment(request):
    form = forms.CommentForm(request.POST)
    in_group_name = request.GET.get('name', 'None')
    in_group = get_object_or_404(Group, name=in_group_name)
    text = form.data['comment']
    new_comment = models.Comment(
        text = text,
        user = request.user,
        group = in_group
    )
    new_comment.save()
    return getGroup(request)


@login_required
def removeComment(request):
    comment_id = request.GET.get('id', 'None')
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return getGroup(request)