from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import AttributeModel, AttributevalueModel
from ..serializers.attribute import (
    CreateAttributeSerializer,
    CreateAttributevalueSerializer,
    ListAttributeSerializer,
    ListAttributevalueSerializer,
    RetrieveAttributeSerializer,
    RetrieveAttributevalueSerializer,
)


@extend_schema(tags=["attribute"])
class AttributeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = AttributeModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListAttributeSerializer
            case "retrieve":
                return RetrieveAttributeSerializer
            case "create":
                return CreateAttributeSerializer
            case _:
                return ListAttributeSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["attributeValue"])
class AttributevalueView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = AttributevalueModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListAttributevalueSerializer
            case "retrieve":
                return RetrieveAttributevalueSerializer
            case "create":
                return CreateAttributevalueSerializer
            case _:
                return ListAttributevalueSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
