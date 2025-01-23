from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import BlogModel
from ..serializers.blog import CreateBlogSerializer, ListBlogSerializer, RetrieveBlogSerializer


@extend_schema(tags=["blog"])
class BlogView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BlogModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListBlogSerializer
            case "retrieve":
                return RetrieveBlogSerializer
            case "create":
                return CreateBlogSerializer
            case _:
                return ListBlogSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
