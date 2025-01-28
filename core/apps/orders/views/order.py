from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import OrderModel, OrderstatusModel
from ..serializers.order import (
    CreateOrderSerializer,
    CreateOrderstatusSerializer,
    ListOrderSerializer,
    ListOrderstatusSerializer,
    RetrieveOrderSerializer,
    RetrieveOrderstatusSerializer,
)


@extend_schema(tags=["OrderStatus"])
class OrderstatusView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = OrderstatusModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListOrderstatusSerializer
            case "retrieve":
                return RetrieveOrderstatusSerializer
            case "create":
                return CreateOrderstatusSerializer
            case _:
                return ListOrderstatusSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["Order"])
class OrderView(BaseViewSetMixin, ModelViewSet):  
    queryset = OrderModel.objects.all()

    def get_serializer_class(self) -> Any:
        if self.action == "list":
            return ListOrderSerializer
        elif self.action == "retrieve":
            return RetrieveOrderSerializer
        elif self.action == "create":
            return CreateOrderSerializer
        else:
            return ListOrderSerializer

    def get_permissions(self) -> Any:
        if self.action in ["create", "update", "delete"]:
            self.permission_classes = [AllowAny]  
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
