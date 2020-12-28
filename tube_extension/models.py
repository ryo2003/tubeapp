from django.db import models
from django.urls import reverse_lazy
from django_mysql.models import ListCharField

# Create your models here.

class Video(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])