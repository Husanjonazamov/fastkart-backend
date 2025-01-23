from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import TransactionModel
from ..serializers.transaction import (
    CreateTransactionSerializer,
    ListTransactionSerializer,
    RetrieveTransactionSerializer,
)


@extend_schema(tags=["transaction"])
class TransactionView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TransactionModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListTransactionSerializer
            case "retrieve":
                return RetrieveTransactionSerializer
            case "create":
                return CreateTransactionSerializer
            case _:
                return ListTransactionSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
