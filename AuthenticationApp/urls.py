"""AuthenticationApp URL Configuration

Created by Naman Patwari on 10/4/2016.
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.auth_login, name='Login'),
    url(r'^logout$', views.auth_logout, name='Logout'),
    url(r'^register$', views.auth_register, name='Register'),
    url(r'^update$', views.update_profile, name='UpdateProfile'),
    url(r'^users$', views.get_users, name='GetUsers'),
    url(r'^user$', views.get_user, name='GetUser'),
    url(r'^mark$', views.add_bookmark, name='AddBookmark'),
    url(r'^unmark$', views.remove_bookmark, name='RemoveBookmark'),
    url(r'^marks$', views.get_bookmarks, name='GetBookmarks')
]