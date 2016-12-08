"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
import tinymce
from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)

class MemberForm(forms.Form):
    email = forms.CharField(label='Email', max_length=50)

class LinkForm(forms.Form):
    project = forms.CharField(label='Name', max_length=100)

class CommentForm(forms.Form):
    comment = forms.CharField(label="comment", widget=tinymce.widgets.TinyMCE(attrs={'cols': 80, 'rows': 5}), required=True)