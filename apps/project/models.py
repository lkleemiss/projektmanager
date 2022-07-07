from django.db import models
from django.contrib.auth.models import User

from apps.userprofile.models import Userprofile


class Project(models.Model):
    # Status
    ACTIVE = 'active'
    OPEN = 'open'
    FINISHED = 'finished'
    CLOSED = 'closed'
    BREAK = 'break'

    CHOICES_STATUS = [
        (ACTIVE, 'Aktiv'),
        (OPEN, 'Offen'),
        (FINISHED, 'Erledigt'),
        (CLOSED, 'Abgebrochen'),
        (BREAK, 'Pause')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, )
    members = models.ManyToManyField(User, related_name='projects')
    manager = models.ForeignKey(User, related_name='manager', on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True)  # saves instance of date-time into the database when the object is created.
    last_change = models.DateTimeField(
        auto_now=True)  # saves instance of date-time into the database when the object is saved.
    deadline_date = models.DateField(blank=True, null=True)  # can be null and is only optional in the form
    status = models.CharField(max_length=15, choices=CHOICES_STATUS, default=OPEN)
    team = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def num_task_done(self):
        return self.tasks.filter(checked=True).count()

    def num_task_todo(self):
        return self.tasks.filter(checked=False).count()

    def tracked_time(self):
        return sum(entry.seconds for entry in self.time_entries.all())

    def progress_percent(self):
        if self.tasks.count() > 0:
            tasks_done = self.tasks.filter(checked=True)
            progress_percent = int((tasks_done.count() * 100) / self.tasks.count())
        else:
            progress_percent = 0
        return progress_percent
