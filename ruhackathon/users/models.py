from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):

    user = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures')
    description = models.TextField(blank=True, max_length=100)
    is_confirmed = models.BooleanField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        """Позволяет получить url профиля внутри шаблона"""
        return reverse('profile-detail', kwargs={'slug':self.user.username})
