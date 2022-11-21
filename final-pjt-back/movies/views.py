from django.contrib.auth import get_user_model

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Genre, Movie, Review
from .serializers import (
    MovieListSerializer, 
    MovieDetailSerializer,
    ReviewSerializer,
    GenreSerializer,
)

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# 영화 목록
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 영화 세부 정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

# 영화 좋아요
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        isLike = False
    else:
        movie.like_users.add(user)
        isLike = True
    context = {
        'isLike' : isLike,
        'like_cnt' : movie.like_users.count()
    }
    return JsonResponse(context)

# 영화별 리뷰 목록
@api_view(['GET'])
def review_list(request, movie_pk):
    reviews = get_list_or_404(Review, movie=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 영화별 리뷰 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

# 영화별 리뷰별 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)