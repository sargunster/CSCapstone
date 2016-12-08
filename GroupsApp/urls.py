"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
    url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/delete$', views.deleteGroup, name='DeleteGroup'),
    url(r'^group/add$', views.addToGroup, name='GroupAdd'),
    url(r'^group/linkform$', views.linkToProject, name='GroupLink'),
    url(r'^group/linkformsuccess$', views.getLinkFormSuccess, name='LinkFormSuccess'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^group/addcomment$', views.addComment, name='AddComment'),
    url(r'^group/removecomment$', views.removeComment, name='RemoveComment')
]