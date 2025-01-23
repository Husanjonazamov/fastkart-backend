from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import PaymentaccountModel
from ..serializers.paymentAccount import (
    CreatePaymentaccountSerializer,
    ListPaymentaccountSerializer,
    RetrievePaymentaccountSerializer,
)


@extend_schema(tags=["paymentAccount"])
class PaymentaccountView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PaymentaccountModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListPaymentaccountSerializer
            case "retrieve":
                return RetrievePaymentaccountSerializer
            case "create":
                return CreatePaymentaccountSerializer
            case _:
                return ListPaymentaccountSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
