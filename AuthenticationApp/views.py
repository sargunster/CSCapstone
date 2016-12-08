"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .forms import LoginForm, RegisterForm, UpdateForm, QualificationsForm
from .models import MyUser

from ProjectsApp.models import Project
from GroupsApp.models import Group
from UniversitiesApp.models import Course

import ProjectsApp.views


# Auth Views

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if next_url is None:
        next_url = "/"
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Success! Welcome, ' + (user.first_name or ""))
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            messages.warning(request, 'Invalid username or password.')

    context = {
        "form": form,
        "page_name": "Login",
        "button_value": "Login",
        "links": ["register"],
    }
    return render(request, 'auth_form.html', context)


def auth_logout(request):
    logout(request)
    messages.success(request, 'Success, you are now logged out')
    return render(request, 'index.html')


def auth_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        new_user = MyUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data["password2"],
                                              first_name=form.cleaned_data['firstname'],
                                              last_name=form.cleaned_data['lastname'],
                                              is_student=form.cleaned_data['student'],
                                              is_professor=form.cleaned_data['professor'],
                                              is_engineer=form.cleaned_data['engineer'],
                                              about=form.cleaned_data['about'])
        new_user.save()
        login(request, new_user)
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'index.html')

    context = {
        "form": form,
        "page_name": "Register",
        "button_value": "Register",
        "links": ["login"],
    }
    return render(request, 'auth_form.html', context)


@login_required
def update_profile(request):
    email = request.GET.get('email', None)
    user = None
    if request.user.is_staff and email is not None:
        user = MyUser.objects.filter(email__exact=email).first()
    if user is None:
        user = request.user
    form = UpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Success, your profile was saved!')

    context = {
        "form": form,
        "page_name": "Update",
        "button_value": "Update",
        "links": ["logout"],
    }
    return render(request, 'auth_form.html', context)


@login_required
def update_qual(request):
    form = QualificationsForm()
    context = {
        "form": form,
        "page_name": "Update",
        "button_value": "Update"
    }
    return render(request, 'qual_form.html', context)


@login_required
def qual_success(request):
    form = QualificationsForm(request.POST)
    request.user.qualifications = form.data['qualifications']
    request.user.specializations = form.data['specializations']
    request.user.experience = form.data['experience']
    context = {
        'user': request.user,
        'can_edit': True
    }
    return render(request, 'user.html', context)


def get_users(request):
    if request.user.is_authenticated():
        users_list = MyUser.objects.all()
        context = {
            'users': users_list,
        }
        return render(request, 'users.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def get_user(request):
    if request.user.is_authenticated():
        in_email = request.GET.get('email', 'None')
        in_user = MyUser.objects.filter(email__exact=in_email).first()
        if in_user is None:
            return render(request, 'notfound.html', status=404)
        context = {
            'user': in_user,
            'can_edit': request.user.email == in_user.email or request.user.is_staff,
            'groups': Group.objects.filter(members__email__exact=in_email),
            'courses': Course.objects.filter(members__email__exact=in_email),
        }
        return render(request, 'user.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


@login_required
def add_bookmark(request):
    user = request.user
    project_name = request.GET.get('name', None)
    project = get_object_or_404(Project, name=project_name)
    user.bookmarks.add(project)
    user.save()
    return ProjectsApp.views.getProject(request)


@login_required
def remove_bookmark(request):
    user = request.user
    project_name = request.GET.get('name', None)
    project = get_object_or_404(Project, name=project_name)
    user.bookmarks.remove(project)
    user.save()
    return ProjectsApp.views.getProject(request)


@login_required
def get_bookmarks(request):
    user = request.user
    projects = user.bookmarks
    return render(request, 'bookmarks.html', {'projects': projects})
