import tinymce.widgets
from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'language', 'experience', 'specialty')


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'language', 'experience', 'specialty')
