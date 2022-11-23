from rest_framework import serializers
from .models import Article, Comment

# 게시글 제목
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'user',)

# 게시글에 대한 세부 정보 (제목, 내용, 생성일자, 수정일자)
class ArticleDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields =('user', 'like_users', 'username',)

# 게시글 하나에 적힌 댓글 목록 / 댓글에 대한 세부 정보 (내용, 생성일자, 수정일자)
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields=('article','user',)