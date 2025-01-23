from rest_framework import serializers

from ...models import WishlistModel


class BaseWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...


class RetrieveWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...


class CreateWishlistSerializer(BaseWishlistSerializer):
    class Meta(BaseWishlistSerializer.Meta): ...
