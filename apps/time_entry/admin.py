from django.contrib import admin

# Import models
from .models import TimeEntry

admin.site.register(TimeEntry)