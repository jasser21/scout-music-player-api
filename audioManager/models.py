from unittest.util import _MAX_LENGTH
from django.db import models


class dropboxToken(models.Model):
    access_token = models.TextField(unique=True)
    user = models.TextField()
    state = models.TextField(blank=True, null=True)


class Song(models.Model):
    file_id = models.CharField(max_length=200, unique=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    is_downloadble = models.BooleanField()
    name = models.CharField(max_length=50)


# Create your models here.
