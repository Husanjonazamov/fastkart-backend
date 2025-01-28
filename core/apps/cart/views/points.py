from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import PointsModel
from ..serializers.points import CreatePointsSerializer, ListPointsSerializer, RetrievePointsSerializer


@extend_schema(tags=["points"])
class PointsView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = PointsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListPointsSerializer
            case "retrieve":
                return RetrievePointsSerializer
            case "create":
                return CreatePointsSerializer
            case _:
                return ListPointsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
