from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    link = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    def __str__(self):
        return self.title
