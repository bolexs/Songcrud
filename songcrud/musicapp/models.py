from email.policy import default
from enum import auto
from importlib.resources import contents
from datetime import date, datetime
from operator import mod
from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length= 40)
    date_released = models.DateTimeField(default=date.today)
    likes = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.CharField(max_length = 1000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.content