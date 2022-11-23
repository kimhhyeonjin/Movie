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
    UserDetailSerializer,
)

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
import json

def vote_avg_sort(arr):
    arr.sort(key=lambda x:x.vote_average, reverse=True)
    return arr[:10]

# 영화 목록
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 평점 순 영화
@api_view(['GET'])
def top_rated(request):
    rated_movies = Movie.objects.all().order_by('-vote_average')[:30]
    serializer = MovieListSerializer(rated_movies, many=True)
    return Response(serializer.data)

# 인기 순 영화
@api_view(['GET'])
def popularity(request):
    rated_movies = Movie.objects.all().order_by('-popularity')[:30]
    serializer = MovieListSerializer(rated_movies, many=True)
    return Response(serializer.data)

# 최근 개봉 영화
@api_view(['GET'])
def upcoming(request):
    rated_movies = Movie.objects.all().order_by('-release_date')[:30]
    serializer = MovieListSerializer(rated_movies, many=True)
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


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def recommend(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movies = get_list_or_404(Movie)
    # print(user)
    # print(user.id)
    # print(movies)
    
    # 좋아하는 영화 정보 가져오기
    like_movies = []
    for movie in movies:
        for like_user in movie.like_users.all():
            if user.id == like_user.id:
                like_movies.append(movie)
                print(movie.id)
    print(like_movies)
    
    # 좋아하는 영화의 장르 id 가져오기
    
    movies = get_list_or_404(Movie)
    # print(movies)
    recommend_list = []
    for movie in movies:
        if movie in like_movies:
            continue
        genre_ids = movie.genre_ids.all()
        for like_movie in like_movies:
            print(like_movie)
            for genre in genre_ids:
                print(genre)
                print(genre.id)
                # if like_movie
                
        

    
        #     genres = movie.genres.all()
        #     # print(movie, genres)
        #     for x in prefer:
        #         for genre in genres:
        #             # print(x, genre.pk)
        #             if x == genre.pk and movie not in recommend_list:
        #                 recommend_list.append(movie)
        # # print(recommend_list, len(recommend_list))
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)
    

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def recommend(request):
#     user = request.user
#     like_movies =  user.like_movies.all()
#     print(like_movies)
#     prefer = []
#     for movie in like_movies:
#         genres = movie.genre_ids.all()
#         for genre in genres:
#             if genre.pk not in prefer:
#                 prefer.append(genre.pk)
#     # print(prefer)
#     movies = list(Movie.objects.all().values())
#     recommend_list = []
#     for movie in movies:
#         print(movie)

#     print(movies)
#     recommend_list = []
#     for movie in movies:
#         if movie in like_movies:
#             continue
#         genres = movie.genre_ids.all()
#         # print(movie, genres)
#         for x in prefer:
#             for genre in genres:
#                 # print(x, genre.pk)
#                 if x == genre.pk and movie not in recommend_list:
#                     recommend_list.append(movie)
#     # print(recommend_list, len(recommend_list))
#     real_recommend = vote_avg_sort(recommend_list)
#     if not real_recommend:
#         real_recommend = vote_avg_sort(movies)
#     context = {
#         'like_movies':like_movies,
#         'real_recommend': real_recommend
#     }
#     return Response(context)

@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def random(request):
    movies = Movie.objects.order_by('?')[:200]
    serializer = MovieDetailSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def userdetail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)