from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta
from django.utils import timezone

from .forms import *
from apps.task.forms import *
from apps.time_entry.models import TimeEntry


@login_required
def project(request, project_id):
    """
    View for project overview and handels forms for creating tasks and time entries and deleting projects
    Provides the project with the given given id and filtered time entries and tasks of the project
    """
    project = get_object_or_404(Project, pk=project_id, members__in=[request.user])

    if request.method == 'POST' and 'createtask_form' in request.POST:
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            member_id = request.POST.get("resp_member_id", None)
            if member_id:
                form.instance.responsible_user = project.members.get(pk=member_id)
            elif not project.members.count() > 1:
                form.instance.responsible_user = request.user

            form.instance.project = project
            form.save()

            messages.info(request, 'Die Aufgabe wurde erstellt')
            return redirect('project', project_id=project_id)
    elif request.method == 'POST' and 'timeentry_form' in request.POST:
        hours = int(request.POST.get('hours', 0))
        minutes = int(request.POST.get('minutes', 0))
        seconds = int(request.POST.get('seconds', 0))
        date = request.POST.get('date', None)
        print(date)

        seconds_total = ((hours * 60) + minutes) * 60 + seconds

        time_entry = TimeEntry.objects.create(project=project, seconds=seconds_total,
                                              created_by=request.user)
        time_entry.date = date
        time_entry.save()

        messages.success(request, 'Deine Zeit wurde gespeichert.')
        return redirect('project', project_id=project_id)
    elif request.method == 'POST' and 'deleteproject_form' in request.POST:
        if project.manager == request.user:
            project.delete()
            messages.success(request, 'Das Projekt wurde gelöscht.')
            return redirect('projects')
        else:
            project.members.remove(request.user)
            messages.success(request, 'Du hast das Projekt verlassen.')
            return redirect('projects')
    else:
        form = CreateTaskForm()

    tasks_todo = project.tasks.filter(checked=False)
    tasks_done = project.tasks.filter(checked=True)

    # Progress of done Tasks
    if project.tasks.count() > 0:
        task_progress = int((project.num_task_done() * 100) / project.tasks.count())
    else:
        task_progress = 0

    tracked_time = timedelta(seconds=project.tracked_time())

    try:
        active_time_entry = request.user.time_entries.filter(is_active=True).latest('start_time')
        print(active_time_entry.id)
        now = timezone.now()

        timesince = now - active_time_entry.start_time

        seconds = int(timesince.total_seconds())

        # get hours and rest of division goes in minutes
        minutes, active_time_seconds = divmod(seconds, 60)
        active_time_hours, active_time_minutes = divmod(minutes, 60)
    except:
        active_time_entry = None
        active_time_hours = None
        active_time_minutes = None
        active_time_seconds = None

    context = {'project': project, 'tasks_todo': tasks_todo, 'tasks_done': tasks_done, 'createtask_form': form,
               'task_progress': task_progress, 'tracked_time': tracked_time,
               'active_time_hours': active_time_hours, 'active_time_minutes': active_time_minutes,
               'active_time_seconds': active_time_seconds, 'active_time_entry': active_time_entry}
    return render(request, 'project/project.html', context)


@login_required()
def delete_project(request, project_id):
    """
    Deletes the project with the given project id and redirects to projects overview
    """
    if Project.objects.get(pk=project_id).manager == request.user:
        Project.objects.get(pk=project_id).delete()

    return redirect('projects')


@login_required
def edit_project(request, project_id):
    """
    Provides Form to edit project and makes it possible to delete project and edit the members
    """
    project = get_object_or_404(Project, pk=project_id, manager=request.user)

    if request.method == 'POST' and 'deletemember_form' in request.POST:
        member_id = request.POST.get("member_id", False)
        member = project.members.get(pk=member_id)
        project.members.remove(member)

        messages.success(request, 'Der User wurde aus dem Projekt entfernt.')
        return redirect('project_edit', project_id=project_id)
    elif request.method == 'POST' and 'deleteproject_form' in request.POST:
        if project.manager == request.user:
            project.delete()
            messages.success(request, 'Das Projekt wurde gelöscht.')
            return redirect('projects')
    elif request.method == 'POST':
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            if not form.cleaned_data['team']:
                members = form.instance.members.exclude(pk=request.user.id)
                for member in members:
                    form.instance.members.remove(member)
            form.save()

            messages.success(request, 'Die Änderungen wurden gespeichert.')
            return redirect('project', project_id=project_id)
        else:
            messages.error(request, 'Daten falsch eingegeben.')
    else:
        form = ProjectEditForm(instance=project)

    return render(request, 'project/editProject.html',
                  {'project': project, 'form': form, })


@login_required
def add_project(request):
    """
    Provides form the create project and saves it
    """
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.instance.manager = request.user
            form.save()
            form.instance.members.add(request.user)
            messages.success(request, 'Projekt gespeichert.')
            return redirect('project', project_id=form.instance.id)
        else:
            messages.error(request, 'Daten falsch eingegeben.')
    else:
        form = ProjectForm()

    return render(request, 'project/addProject.html', {'form': form, })


@login_required
def projects(request):
    """
        Provides all project of user and sort them by the date of the last change
    """
    projects = request.user.projects.all().order_by('-last_change')

    if request.method == 'POST' and 'deleteproject_form' in request.POST:
        project_id = request.POST.get("project_id", False)
        project = get_object_or_404(Project, pk=project_id)
        if project.manager == request.user:
            project.delete()
            messages.success(request, 'Das Projekt wurde gelöscht.')
        else:
            project.members.remove(request.user)
            messages.success(request, 'Du hast das Projekt verlassen.')

    context = {'projects': projects, }

    return render(request, 'project/projects.html', context)


@login_required()
def project_new_member(request, project_id):
    """
    Adds new member to given project
    """
    project = get_object_or_404(Project, pk=project_id)
    member_email = request.POST.get('email', None)

    if member_email:
        user = User.objects.get(username=member_email)
        project.members.add(user)

    return HttpResponse()


@login_required()
def start_time(request, project_id):
    """
    Creates time entry for the live tracking timer
    Returns id of the created time entry
    """
    project = get_object_or_404(Project, pk=project_id)

    time_entry = TimeEntry.objects.create(project=project, created_by=request.user, is_active=True)
    time_entry.save()

    return HttpResponse(time_entry.id, content_type='text/plain')


@login_required()
def add_time_entry(request, project_id):
    """
    Adds new time entry with time data from the form
    """
    active_time_entry_id = request.POST.get('id', None)

    hours = int(request.POST.get('hours', 0))
    minutes = int(request.POST.get('minutes', 0))
    seconds = int(request.POST.get('seconds', 0))
    seconds_total = ((hours * 60) + minutes * 60) + seconds

    if active_time_entry_id:
        active_time_entry = get_object_or_404(TimeEntry, pk=active_time_entry_id)
        active_time_entry.is_active = False
        active_time_entry.seconds = seconds_total
        active_time_entry.save()

    return HttpResponse()
