from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/static/images/user_placeholder.png'
