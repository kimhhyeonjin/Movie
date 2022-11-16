from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    genre_ids = models.ManyToManyField(Genre)
    overview = models.TextField()
    vote_average=models.FloatField()
    poster_path=models.CharField(max_length=200)
    backdrop_path=models.CharField(max_length=200)
