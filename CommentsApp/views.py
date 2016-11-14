from django.shortcuts import render

from . import forms
from . import models


# Create your views here.
def get_comments(request):
    comments_list = models.Comment.objects.all()
    context = {
        'comments': comments_list,
    }
    return render(request, 'comments.html', context)


def get_comment_form(request):
    return render(request, 'commentForm.html')


def add_comment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'])
            new_comment.save()
        else:
            form = forms.CommentForm()
    return get_comments(request)
