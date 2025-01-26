from rest_framework import serializers

from ...models import WishlistModel
from .wishlistitem import ListWishlistItemSerializer
from core.apps.accounts.serializers.user import UserSerializer

class BaseWishlistSerializer(serializers.ModelSerializer):
    items = ListWishlistItemSerializer(many=True, read_only=True)
    consumer = UserSerializer()

    class Meta:
        model = WishlistModel
        fields = [
            "id",
            "items",
            "consumer",
            "total",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at"
        ]


class ListWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...


class RetrieveWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...


class CreateWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...
