from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from postsApi.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('id','author','body','created_at','updated_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields =('id','username')    