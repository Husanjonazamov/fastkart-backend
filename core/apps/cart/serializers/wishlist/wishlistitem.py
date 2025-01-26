from rest_framework import serializers

from ...models import WishlistitemModel
from core.apps.product.serializers.product import ListProductSerializer


class BaseWishlistItemSerializer(serializers.ModelSerializer):
    product = ListProductSerializer()
    
    class Meta:
        model = WishlistitemModel
        fields = [
            "id",
            "wishlist",
            "product",
            "created_at",
            "updated_at",
            "deleted_at",
        ]
        
        read_only_fields = [
            "created_at",
            "updated_at",
            "deleted_at"
        ]



class ListWishlistItemSerializer(BaseWishlistItemSerializer):
    class Meta(BaseWishlistItemSerializer.Meta): ...


class RetrieveWishlistItemSerializer(BaseWishlistItemSerializer):
    class Meta(BaseWishlistItemSerializer.Meta): ...


class CreateWishlistItemSerializer(BaseWishlistItemSerializer):
    class Meta(BaseWishlistItemSerializer.Meta): ...
