from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(label='name', max_length=200)
    description = forms.CharField(label='description', max_length=10000)
    language = forms.CharField(label='language', max_length=200, initial=None)
    experience = forms.CharField(label='experience', max_length=200, initial=None)
    specialty = forms.CharField(label='specialty', max_length=200, initial=None)