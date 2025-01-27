from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import CompareitemModel, CompareModel
from ..serializers.compare import (
    CreateCompareitemSerializer,
    CreateCompareSerializer,
    ListCompareitemSerializer,
    ListCompareSerializer,
    RetrieveCompareitemSerializer,
    RetrieveCompareSerializer,
)


@extend_schema(tags=["compare"])
class CompareView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = CompareModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCompareSerializer
            case "retrieve":
                return RetrieveCompareSerializer
            case "create":
                return CreateCompareSerializer
            case _:
                return ListCompareSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["compareItem"])
class CompareitemView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CompareitemModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCompareitemSerializer
            case "retrieve":
                return RetrieveCompareitemSerializer
            case "create":
                return CreateCompareitemSerializer
            case _:
                return ListCompareitemSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
