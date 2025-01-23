from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import WishlistModel
from ..serializers.wishlist import CreateWishlistSerializer, ListWishlistSerializer, RetrieveWishlistSerializer


@extend_schema(tags=["wishlist"])
class WishlistView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = WishlistModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListWishlistSerializer
            case "retrieve":
                return RetrieveWishlistSerializer
            case "create":
                return CreateWishlistSerializer
            case _:
                return ListWishlistSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
