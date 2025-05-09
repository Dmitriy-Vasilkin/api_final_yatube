from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Разрешение запросов для пользователей."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
