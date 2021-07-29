from rest_framework import serializers
from  postsApi.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','author','title','body','created_at','updated_at')

