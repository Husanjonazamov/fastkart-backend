from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import VariationModel
from ..serializers.variation import CreateVariationSerializer, ListVariationSerializer, RetrieveVariationSerializer


@extend_schema(tags=["variation"])
class VariationView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = VariationModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListVariationSerializer
            case "retrieve":
                return RetrieveVariationSerializer
            case "create":
                return CreateVariationSerializer
            case _:
                return ListVariationSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
