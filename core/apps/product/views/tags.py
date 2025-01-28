from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import TagsModel
from ..serializers.tags import CreateTagsSerializer, ListTagsSerializer, RetrieveTagsSerializer


@extend_schema(tags=["tags"])
class TagsView(BaseViewSetMixin, ModelViewSet):
    queryset = TagsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListTagsSerializer
            case "retrieve":
                return RetrieveTagsSerializer
            case "create":
                return CreateTagsSerializer
            case _:
                return ListTagsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
