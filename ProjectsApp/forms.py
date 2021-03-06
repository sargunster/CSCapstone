import tinymce.widgets
from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'language', 'experience', 'specialty')
        labels = {
            'language': 'Programming Languages (comma-separated)',
            'experience': 'Years of experience',
            'specialty': 'Specializations (comma-separated)'
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'language', 'experience', 'specialty')
        labels = {
            'language': 'Programming Languages (comma-separated)',
            'experience': 'Years of experience',
            'specialty': 'Specializations (comma-separated)'
        }
