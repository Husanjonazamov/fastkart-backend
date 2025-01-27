from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import CategoryModel
from ..serializers.category import CreateCategorySerializer, ListCategorySerializer, RetrieveCategorySerializer



@extend_schema(tags=["category"])
class CategoryView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = CategoryModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCategorySerializer
            case "retrieve":
                return RetrieveCategorySerializer
            case "create":
                return CreateCategorySerializer
            case _:
                return ListCategorySerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
