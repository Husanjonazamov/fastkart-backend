from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import CountryModel
from ..serializers.country import CreateCountrySerializer, ListCountrySerializer, RetrieveCountrySerializer


@extend_schema(tags=["Country"])
class CountryView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = CountryModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCountrySerializer
            case "retrieve":
                return RetrieveCountrySerializer
            case "create":
                return CreateCountrySerializer
            case _:
                return ListCountrySerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
