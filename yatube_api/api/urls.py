from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupsViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/groups', GroupsViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
    basename='comments'
)
router.register(r'v1/follow', FollowViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
