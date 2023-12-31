from django.urls import path
from . import views

# 상위 주소 : path('movies/', include('movies.urls'))
urlpatterns = [
    # 전체 영화 리스트 
    path('', views.movie_list),
    # 평점 순 영화 리스트
    path('top-rated/', views.top_rated),
    # 인기 순 영화 리스트
    path('popularity/', views.popularity),
    # 최근 개봉 및 예정 영화 리스트
    path('upcoming/', views.upcoming),
    # 개별 영화 정보
    path('<int:movie_pk>/', views.movie_detail),
    # 영화 좋아요
    path('<int:movie_pk>/likes/', views.movie_like),
    # 영화별 리뷰 생성
    path('<int:movie_pk>/create_review/', views.create_review),
    # 영화별 리뷰 목록
    path('<int:movie_pk>/reviews/', views.review_list),
    # 개별 리뷰 정보
    path('reviews/<int:review_pk>/', views.review_detail),
    # 추천 영화 : 랜덤
    path('random/', views.random),
    # 추천 영화 : 좋아요 기반
    path('recommend/<int:user_pk>/', views.recommend),
    # 유저 정보
    path('userdetail/<int:user_pk>/', views.userdetail),
    # 좋아요 한 영화정보 가져오기
    path('like_movies/<int:user_pk>/', views.like_movies),
]

