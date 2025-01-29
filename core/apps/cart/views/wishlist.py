from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import WishlistModel, WishlistitemModel
from ..serializers.wishlist import CreateWishlistSerializer, ListWishlistSerializer, RetrieveWishlistSerializer
from ..serializers.wishlist.wishlistitem import (
    ListWishlistItemSerializer,
    RetrieveWishlistItemSerializer,
    CreateWishlistItemSerializer,
)

@extend_schema(tags=["wishlist"])
class WishlistView(BaseViewSetMixin, ModelViewSet):
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



@extend_schema(tags=["wishlist_item"])
class WishlistItemView(BaseViewSetMixin, ModelViewSet):
    queryset = WishlistitemModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListWishlistItemSerializer
            case "retrieve":
                return RetrieveWishlistItemSerializer
            case "create":
                return CreateWishlistItemSerializer
            case _:
                return ListWishlistItemSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
