from django.db import models
from django.conf import settings
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

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()