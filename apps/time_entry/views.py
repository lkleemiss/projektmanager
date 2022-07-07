from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import TimeEntry
from apps.task.models import Task
from apps.project.models import Project


@login_required()
def edit_time_entry(request, project_id, time_entry_id, task_id=None):
    """
        Provides form to edit a existing time_entry
    """
    project = get_object_or_404(Project, pk=project_id)
    time_entry = get_object_or_404(TimeEntry, pk=time_entry_id)
    try:
        task = get_object_or_404(Task, pk=task_id)
    except:
        task = None

    if request.method == 'POST':
        hours = int(request.POST.get('hours', 0))
        minutes = int(request.POST.get('minutes', 0))
        seconds = int(request.POST.get('seconds', 0))
        date = request.POST.get('date', None)

        seconds_total = ((hours * 60) + minutes) * 60 + seconds

        time_entry.date = date
        time_entry.seconds = seconds_total
        time_entry.save()

        messages.success(request, 'Deine Zeit wurde gespeichert.')

        return redirect('project', project_id=project_id)

    # seperate seocnds in sec, min and hours
    minutes, seconds = divmod(time_entry.seconds, 60)
    hours, minutes = divmod(minutes, 60)

    context = {
        'project': project, 'task': task, 'time_entry': time_entry, 'hours': hours, 'minutes': minutes,
        'seconds': seconds,
    }

    return render(request, 'time_entry/editTimeEntry.html', context)


@login_required()
def delete_time_entry(request, project_id, time_entry_id):
    """
        Deletes the time_entry with given id
    """
    time_entry = get_object_or_404(TimeEntry, pk=time_entry_id).delete()
    messages.success(request, 'Der Zeit Eintrag wurde entfernt.')
    return redirect('project', project_id=project_id)
