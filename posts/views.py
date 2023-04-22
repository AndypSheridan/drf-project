from rest_framework import permissions, generics
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
