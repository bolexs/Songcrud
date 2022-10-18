from importlib.resources import contents
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length= 40)
    data_released = models.DateField()
    likes = models.IntegerField(max_length = 10)
    artist_id = models.ForeignKey(Artist, on_delete = models.CASCADE)


class Lyrics(models.Model):
    content = models.CharField(max_length = 1000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)