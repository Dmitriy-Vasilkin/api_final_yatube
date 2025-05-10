from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор модели Follow."""

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Follow
        exclude = ('id',)

    def validate_following(self, value):
        current_user = self.context.get('request').user
        if not value:
            raise ValidationError('"following" обязательно для заполнения.')
        try:
            publisher = User.objects.get(username=value)
            if Follow.objects.filter(
                user=current_user, following=publisher
            ).first():
                raise ValidationError('Вы уже подписаны.')
            if current_user == publisher:
                raise ValidationError('Нельзя подписываться на себя.')
        except User.DoesNotExist:
            raise ValidationError('Автор не найден.')
        return value
