from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CurrencyModel
from ..serializers.currency import CreateCurrencySerializer, ListCurrencySerializer, RetrieveCurrencySerializer


@extend_schema(tags=["Currency"])
class CurrencyView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CurrencyModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCurrencySerializer
            case "retrieve":
                return RetrieveCurrencySerializer
            case "create":
                return CreateCurrencySerializer
            case _:
                return ListCurrencySerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
