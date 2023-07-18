from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post, User

from .permissions import OwnerOnlyPermission
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupsSerializer,
    PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """Представление для работы с моделью Post."""

    queryset: QuerySet[Post] = Post.objects.all()
    serializer_class: type[PostSerializer] = PostSerializer
    pagination_class: type[LimitOffsetPagination] = LimitOffsetPagination
    permission_classes: tuple[
        type[permissions.BasePermission],
        type[OwnerOnlyPermission]
    ] = (
        permissions.IsAuthenticatedOrReadOnly,
        OwnerOnlyPermission,
    )

    def perform_create(self, serializer: PostSerializer) -> None:
        """Сохраняет автора текущего пользователя в качестве автора поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для работы с моделью Comment."""

    serializer_class: type[CommentSerializer] = CommentSerializer
    permission_classes: tuple[
        type[permissions.BasePermission],
        type[OwnerOnlyPermission]
    ] = (
        permissions.IsAuthenticatedOrReadOnly,
        OwnerOnlyPermission,
    )

    def get_queryset(self) -> QuerySet[Comment]:
        """Возвращает запрос для получения комментариев конкретного поста."""
        post_id: int = self.kwargs.get('post_id')
        post: Post = get_object_or_404(Post, pk=post_id)
        return post.comments

    def perform_create(self, serializer) -> None:
        """
        Сохраняет автора текущего пользователя в качестве автора поста.

        Сохраняет ссылку на указанный пост.
        """
        post_id: int = self.kwargs.get('post_id')
        author: User = self.request.user
        post: Post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=author, post=post)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для работы с моделью Group."""

    queryset: QuerySet[Group] = Group.objects.all()
    serializer_class: type[GroupsSerializer] = GroupsSerializer
    permission_classes: tuple[type[OwnerOnlyPermission]] = (
        OwnerOnlyPermission,
    )


class FollowViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """Представление для работы с моделью Follow."""

    queryset: QuerySet[Follow] = Follow.objects.all()
    serializer_class: type[FollowSerializer] = FollowSerializer
    filter_backends: type[type[filters.BaseFilterBackend]] = (
        filters.SearchFilter,
    )
    search_fields: tuple[str] = ('user__username', 'following__username')

    def get_queryset(self) -> QuerySet[Follow]:
        """Возвращает объекты Follow, относящихся к данному пользователю."""
        user: User = get_object_or_404(User, username=self.request.user)
        return user.follower

    def perform_create(self, serializer: FollowSerializer) -> None:
        """Сохраняет созданный объект с указанием текущего пользователя."""
        serializer.save(user=self.request.user)
