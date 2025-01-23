from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import QuestionsModel
from ..serializers.questions import CreateQuestionsSerializer, ListQuestionsSerializer, RetrieveQuestionsSerializer


@extend_schema(tags=["questions"])
class QuestionsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = QuestionsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListQuestionsSerializer
            case "retrieve":
                return RetrieveQuestionsSerializer
            case "create":
                return CreateQuestionsSerializer
            case _:
                return ListQuestionsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
