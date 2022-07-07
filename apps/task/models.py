from django.db import models
from django.contrib.auth.models import User

# Import models
from apps.userprofile.models import Userprofile
from apps.project.models import Project


# Models
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, )
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    responsible_user = models.ForeignKey(User, related_name='tasks', blank=True, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(blank=True, null=True)  # can be null and is only optional in the form
    deadline_time = models.TimeField(blank=True, null=True)
    checked = models.BooleanField(default=False)

    class Meta:
        # - -> das neuste zuerst
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def tracked_time(self):
        return sum(entry.minutes for entry in self.time_entries.all())
