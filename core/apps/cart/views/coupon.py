from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import CouponModel
from ..serializers.coupon import CreateCouponSerializer, ListCouponSerializer, RetrieveCouponSerializer


@extend_schema(tags=["coupon"])
class CouponView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = CouponModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCouponSerializer
            case "retrieve":
                return RetrieveCouponSerializer
            case "create":
                return CreateCouponSerializer
            case _:
                return ListCouponSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
