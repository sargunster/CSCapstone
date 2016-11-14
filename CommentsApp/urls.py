from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^comments$', views.get_comments, name='Comments'),
    url(r'^commentform$', views.get_comment_form, name='CommentForm'),
    url(r'^addcomment$', views.add_comment, name='AddComment'),
]
