from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import ReviewModel
from ..serializers.review import CreateReviewSerializer, ListReviewSerializer, RetrieveReviewSerializer


@extend_schema(tags=["review"])
class ReviewView(BaseViewSetMixin, ModelViewSet):
    queryset = ReviewModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListReviewSerializer
            case "retrieve":
                return RetrieveReviewSerializer
            case "create":
                return CreateReviewSerializer
            case _:
                return ListReviewSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
