# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Genre, Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
