from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import NotificationModel
from ..serializers.notification import (
    CreateNotificationSerializer,
    ListNotificationSerializer,
    RetrieveNotificationSerializer,
)


@extend_schema(tags=["notification"])
class NotificationView(BaseViewSetMixin, ReadOnlyModelViewSet, ModelViewSet):
    queryset = NotificationModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListNotificationSerializer
            case "retrieve":
                return RetrieveNotificationSerializer
            case "create":
                return CreateNotificationSerializer
            case _:
                return ListNotificationSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
