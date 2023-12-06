from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', default='profile_pics/default_profile.png')

    def __str__(self):
        return f'{self.user.username} Profile'
