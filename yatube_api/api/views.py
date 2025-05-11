from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)

from api.permissions import IsAuthor
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from posts.models import Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет Comment."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]

    def get_queryset(self):
        return self.get_post().comments.all()

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """Вьюсет Follow."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.subscribers.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
