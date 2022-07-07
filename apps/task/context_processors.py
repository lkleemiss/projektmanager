from datetime import datetime, timedelta


def user_tasks(request):
    if request.user.is_authenticated:
        today = datetime.today().date()
        tomorrow = today + timedelta(days=1)

        user_tasks = request.user.tasks.all()
        tasks_done = user_tasks.filter(checked=True)
        tasks_todo = user_tasks.filter(checked=False)
        tasks_today = tasks_todo.filter(deadline_date=today)
        tasks_overdue = tasks_todo.filter(deadline_date__lt=today)
        tasks_tomorrow = tasks_todo.filter(deadline_date=tomorrow)
        tasks_upcoming = tasks_todo.filter(deadline_date__gt=tomorrow)

        if user_tasks.count() > 0:
            tasks_progress = int((tasks_done.count() * 100) / user_tasks.count())
        else:
            tasks_progress = None

        return {'tasks': request.user.tasks.all().order_by('-deadline_date'), 'tasks_done': tasks_done,
                'tasks_todo': tasks_todo, 'tasks_today': tasks_today, 'tasks_overdue': tasks_overdue,
                'tasks_tomorrow': tasks_tomorrow, 'tasks_upcoming': tasks_upcoming, 'tasks_progress': tasks_progress}
    return {}
