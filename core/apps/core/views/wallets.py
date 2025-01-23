from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import WalletsModel
from ..serializers.wallets import CreateWalletsSerializer, ListWalletsSerializer, RetrieveWalletsSerializer


@extend_schema(tags=["wallets"])
class WalletsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = WalletsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListWalletsSerializer
            case "retrieve":
                return RetrieveWalletsSerializer
            case "create":
                return CreateWalletsSerializer
            case _:
                return ListWalletsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
