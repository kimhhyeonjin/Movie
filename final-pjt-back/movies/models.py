from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    genre_list = models.ManyToManyField(Genre)
    
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    overview = models.TextField()
    vote_average=models.FloatField()
    poster_path=models.CharField(max_length=200)
    backdrop_path=models.CharField(max_length=200)
    popularity=models.FloatField()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    content = models.TextField()