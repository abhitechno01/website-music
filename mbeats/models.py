#from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
import datetime
#from .custom_validator import restrict_validator

# Create your models here.
class Artist(models.Model):
    artist = models.CharField(max_length=40, unique=True)
    age = models.IntegerField(default=20, validators = [MaxValueValidator(75)])
    country = models.CharField(max_length=30, default='USA')
    height = models.FloatField(default=1.3, validators = [MaxValueValidator(2.2)])
    photo = models.ImageField(upload_to='artist/')
    def __str__(self):
        return self.artist

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=15)
    year = models.DateField(default=datetime.date(2017,1,1))
    song_toupload = models.FileField(upload_to='songs/')#restrict_validator.ContentTypeRestrictedFileField(upload_to='songs/', content_types=['audio/mp3'], max_upload_size= 21000000)
    song_cover = models.ImageField(upload_to='songs_cover/')


    def __str__(self):
        return self.song_title + ' by ' + self.artist




