from rest_framework import generics,permissions
from postsApi.models import Post
from .serializers import PostSerializer
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=(permissions.IsAuthenticated,)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =(permissions.IsAuthenticated,)