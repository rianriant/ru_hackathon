from django.db import models
from django.utils import timezone
from django.urls import reverse
from cities_light.models import City
from ckeditor.fields import RichTextField
from PIL import Image
from django.contrib.auth.models import User
from users.models import Profile
from tinymce.models import HTMLField



class Ivent(models.Model):
    """Ivent Data"""
    title = models.CharField(max_length=64)
    description = HTMLField(blank=True)
    area = models.ForeignKey(City, on_delete=models.CASCADE, default=City.objects.get(name='Moscow').id)
    address = models.TextField(max_length=124, blank=True)

    created_by = models.ForeignKey(Profile, 
        on_delete=models.CASCADE, 
        related_name='ivents', 
        #default=User.objects.get(username='admin1').pk,

    )

    date_posted = models.DateTimeField(default=timezone.now)
    reg_start_date = models.DateTimeField(default=timezone.now)
    reg_finish_date = models.DateTimeField(default=timezone.now)
    ivent_start_date = models.DateTimeField(default=timezone.now)
    ivent_finish_date = models.DateTimeField(default=timezone.now)

    # This method represents distinct instance of the class as a string
    def __str__(self):
        return self.title

    # Returns URL referenced to DetailView for the instance
    def get_absolute_url(self):
        return reverse('ivent-detail', kwargs = {'pk': self.pk})

