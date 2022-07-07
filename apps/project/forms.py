from django.forms import *
from django import forms

from apps.project.models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('manager', 'members')
        labels = {'title': 'Titel', 'status': 'Status', 'description': 'Beschreibung',
                  'team': 'Handelt es sich um ein Projekt im Team?', 'deadline_date': 'Deadline'}
        widgets = {
            'deadline_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
        }


class ProjectEditForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('manager', 'members')
        labels = {'title': 'Titel', 'status': 'Status', 'description': 'Beschreibung',
                  'team': 'Handelt es sich um ein Projekt im Team?', 'deadline_date': 'Deadline'}
        widgets = {
            'deadline_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
        }


class FolderForm(ModelForm):
    class Meta:
        exclude = ('projects', 'user')
        labels = {'title': 'Titel'}
