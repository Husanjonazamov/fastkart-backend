from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ProductModel
from ..serializers.product import CreateProductSerializer, ListProductSerializer, RetrieveProductSerializer


@extend_schema(tags=["product"])
class ProductView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListProductSerializer
            case "retrieve":
                return RetrieveProductSerializer
            case "create":
                return CreateProductSerializer
            case _:
                return ListProductSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
