from django.urls import path
from . import views

urlpatterns = [
    # 전체 게시글 조회 및 생성
    path('articles/', views.article_list),
    # 게시글 세부 정보 조회, 수정, 삭제
    path('articles/<int:article_pk>/', views.article_detail),
    # 댓글 목록 조회
    path('comments/', views.comment_list),
    # 댓글 세부 정보 조회, 수정, 삭제
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
