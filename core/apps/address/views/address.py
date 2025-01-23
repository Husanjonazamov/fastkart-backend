from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import AddressModel
from ..serializers.address import CreateAddressSerializer, ListAddressSerializer, RetrieveAddressSerializer


@extend_schema(tags=["Address"])
class AddressView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = AddressModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListAddressSerializer
            case "retrieve":
                return RetrieveAddressSerializer
            case "create":
                return CreateAddressSerializer
            case _:
                return ListAddressSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
