from django.contrib import admin

# Register your models here.

#Import models

from .models import Userprofile

#Register
admin.site.register(Userprofile)