from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """Пагинатор для viewset Post."""

    def paginate_queryset(self, queryset, request, view=None):
        if ('limit' not in request.query_params
                and 'offset' not in request.query_params):
            return None
        return super().paginate_queryset(queryset, request, view)
