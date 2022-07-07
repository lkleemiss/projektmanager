from django.db import models
from django.contrib.auth.models import User

from apps.project.models import Project
from apps.task.models import Task


class TimeEntry(models.Model):
    project = models.ForeignKey(Project, related_name='time_entries', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='time_entries', blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    seconds = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='time_entries', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Time Entries'

    def __str__(self):
        if self.task:
            return '%s - %s' % (self.task.title, self.date)  # Positional arguments -> Ausgabe: Titel - Zeitpunkt
        return '%s' % self.date

    def time_in_min(self):
        total_minutes = int(self.seconds / 60)
        return total_minutes
