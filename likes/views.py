from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Likes
from likes.serializers import LikesSerializer


class LikesList(generics.ListCreateAPIView):
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
