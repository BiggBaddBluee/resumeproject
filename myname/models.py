from django.db import models
from django.urls import reverse
# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=500)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sucMsg.html')