from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_api_v1 = DefaultRouter()
router_api_v1.register('posts', PostViewSet, basename='posts')
router_api_v1.register('groups', GroupViewSet, basename='groups')
router_api_v1.register('follow', FollowViewSet, basename='follows')
router_api_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

path_api_v1 = [
    path('', include(router_api_v1.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(path_api_v1)),
]
