from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)

from api.paginators import CustomLimitOffsetPagination
from api.permissions import IsAuthor
from api.serializers import (
    CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
)
from posts.models import Group, Post, User


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет Comment."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    pagination_class = None

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    pagination_class = CustomLimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет Follow."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_subscriber(self):
        return get_object_or_404(User, username=self.request.user)

    def get_queryset(self):
        return self.get_subscriber().subscribers.all()

    def perform_create(self, serializer):
        publisher_name = self.request.data.get('following')
        if not publisher_name:
            raise ValidationError('"following" обязательно для заполнения.')
        try:
            publisher = User.objects.get(username=publisher_name)
            if self.get_queryset().exists():
                raise ValidationError('Вы уже подписаны.')
            if self.request.user == publisher:
                raise ValidationError('Нельзя подписываться на себя.')
            serializer.save(user=self.request.user, following=publisher)
        except User.DoesNotExist:
            raise ValidationError('Автор не найден.')
