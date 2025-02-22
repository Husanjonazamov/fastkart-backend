from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import RefundModel
from ..serializers.refund import CreateRefundSerializer, ListRefundSerializer, RetrieveRefundSerializer


@extend_schema(tags=["Refund"])
class RefundView(BaseViewSetMixin, ModelViewSet):
    queryset = RefundModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListRefundSerializer
            case "retrieve":
                return RetrieveRefundSerializer
            case "create":
                return CreateRefundSerializer
            case _:
                return ListRefundSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
