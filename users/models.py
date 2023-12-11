from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', default='profile_pics/default_profile.png')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()

    #     img = Image.open(self.profile_picture.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
