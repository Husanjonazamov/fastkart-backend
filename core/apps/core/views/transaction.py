from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_core.paginations import CustomPagination



from ..models import TransactionModel
from ..serializers.transaction import (
    CreateTransactionSerializer,
    ListTransactionSerializer,
    RetrieveTransactionSerializer,
)


@extend_schema(tags=["transaction"])
class TransactionView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TransactionModel.objects.all()
    pagination_class = CustomPagination 

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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)