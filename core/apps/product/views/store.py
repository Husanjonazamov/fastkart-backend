from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import StoreModel
from ..serializers.store import CreateStoreSerializer, ListStoreSerializer, RetrieveStoreSerializer


@extend_schema(tags=["store"])
class StoreView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = StoreModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListStoreSerializer
            case "retrieve":
                return RetrieveStoreSerializer
            case "create":
                return CreateStoreSerializer
            case _:
                return ListStoreSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
