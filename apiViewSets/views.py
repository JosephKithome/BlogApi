from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import PostSerializer,UserSerializer
from postsApi.models import Post
from customPermissionApi.permissions import IsAuthorOrReadOnly


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class =PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset =get_user_model().objects.all()
    serializer_class = UserSerializer
