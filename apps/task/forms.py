from django.forms import *
from django import forms

from apps.task.models import *


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('categories', 'project', 'checked', 'responsible_user')
        labels = {'title': 'Titel', 'description': 'Beschreibung', 'deadline_date': 'Tag', 'deadline_time': 'Uhrzeit'}
        widgets = {
            'deadline_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'deadline_time': forms.DateInput(attrs={'type': 'time'})
        }


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('categories', 'project', 'responsible_user')
        labels = {'title': 'Titel', 'description': 'Beschreibung', 'deadline_date': 'Tag', 'deadline_time': 'Uhrzeit',
                  'checked': 'Erledigt?'}
        widgets = {
            'deadline_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'deadline_time': forms.DateInput(attrs={'type': 'time'})
        }
