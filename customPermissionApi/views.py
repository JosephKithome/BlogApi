from rest_framework import generics
from postsApi.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from  apiViewSets.serializers import UserSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=(IsAuthorOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class=UserSerializer   
          

    