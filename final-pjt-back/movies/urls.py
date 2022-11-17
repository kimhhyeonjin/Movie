from django.urls import path
from . import views

# 상위 주소 : path('movies/', include('movies.urls'))
urlpatterns = [
    # 전체 영화 리스트 
    path('', views.movie_list),
    # 개별 영화 정보
    path('<int:movie_pk>/', views.movie_detail),
]

