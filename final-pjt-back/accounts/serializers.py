from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import GenreSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies', 'password', 'email', 'followings', 'reviews', 'followers',)
        # fields = '__all__'
        read_only_fields = ('followings', 'reviews', 'like_movies', 'followers',)