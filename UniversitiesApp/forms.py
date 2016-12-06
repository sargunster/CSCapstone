"""
UniversitiesApp Forms

Created by Jacob Dunbar on 11/5/2016.
"""
from django import forms


class UniversityForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    photo = forms.ImageField(label='Photo')
    description = forms.CharField(label='Description', max_length=300)
    website = forms.CharField(label='Website', max_length=300)


class CourseForm(forms.Form):
    tag = forms.CharField(label='Tag', max_length=10)
    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(label='Description', max_length=300)
    professor = forms.CharField(label="Professor's Email", max_length=100)

class StudentForm(forms.Form):
    email = forms.CharField(label='Email', max_length=50)
