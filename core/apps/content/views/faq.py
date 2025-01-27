from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import FaqModel
from ..serializers.faq import CreateFaqSerializer, ListFaqSerializer, RetrieveFaqSerializer


@extend_schema(tags=["faq"])
class FaqView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = FaqModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListFaqSerializer
            case "retrieve":
                return RetrieveFaqSerializer
            case "create":
                return CreateFaqSerializer
            case _:
                return ListFaqSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
