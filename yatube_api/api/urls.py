from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupsViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"groups", GroupsViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router.register(r"follow", FollowViewSet)

urlpatterns = [
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),
]
