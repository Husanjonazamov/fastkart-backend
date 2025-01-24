from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ImageModel
from ..serializers.image import CreateImageSerializer, ListImageSerializer, RetrieveImageSerializer


@extend_schema(tags=["Image"])
class ImageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ImageModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListImageSerializer
            case "retrieve":
                return RetrieveImageSerializer
            case "create":
                return CreateImageSerializer
            case _:
                return ListImageSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
