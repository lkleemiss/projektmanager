from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .forms import *
from apps.project.models import Project


@login_required
def task(request, project_id, task_id):
    """
      View for task detail view
    """
    project = get_object_or_404(Project, pk=project_id, members__in=[request.user])
    task = get_object_or_404(Task, pk=task_id)

    return render(request, 'task/task.html', {'task': task, 'project': project})


@login_required
def edit_task(request, project_id, task_id):
    """
    Provides form to edit a task
    """
    project = get_object_or_404(Project, pk=project_id, members__in=[request.user])
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            member_id = request.POST.get("resp_member_id", False)
            if member_id:
                form.instance.responsible_user = project.members.get(pk=member_id)

            form.instance.project = project
            form.save()

            messages.info(request, 'Die Änderungen wurden gespeichert.')

            return redirect('project', project_id=project_id)
    else:
        form = EditTaskForm(instance=task)

    return render(request, 'task/editTask.html', {'task': task, 'project': project, 'form': form})


@login_required()
def delete_task(request, project_id, task_id):
    """
    Deletes task with the given id
    """
    if request.user in Project.objects.get(pk=project_id).members.all():
        Task.objects.get(pk=task_id).delete()

    return redirect('project', project_id=project_id)


@login_required()
def update_task(request, project_id, task_id):
    """
        updates the status of the task
    """
    if request.user in Project.objects.get(pk=project_id).members.all():
        task = Task.objects.get(pk=task_id)
        if task.checked:
            task.checked = False
        else:
            task.checked = True
        task.save()
    return HttpResponse('')
