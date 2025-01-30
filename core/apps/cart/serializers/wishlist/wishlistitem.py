from rest_framework import serializers
from ...models import WishlistitemModel, WishlistModel
from core.apps.product.models import ProductModel
from core.apps.product.serializers.product import ListProductSerializer


class BaseWishlistItemSerializer(serializers.ModelSerializer):
    """
    Wishlist itemlar uchun asosiy serializer.
    WishlistItem ichida product obyekti bor bo‘lsa, uni ListProductSerializer yordamida chiqaradi.
    """
    product = ListProductSerializer(read_only=True)  

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
    """
    WishlistItem ro‘yxatini chiqarish uchun serializer.
    BaseWishlistItemSerializer'dan meros oladi.
    """
    class Meta(BaseWishlistItemSerializer.Meta):
        pass


class RetrieveWishlistItemSerializer(BaseWishlistItemSerializer):
    """
    WishlistItem'ni bitta ID orqali olish uchun serializer.
    """
    class Meta(BaseWishlistItemSerializer.Meta):
        pass


class CreateWishlistItemSerializer(BaseWishlistItemSerializer):
    product = serializers.IntegerField()  
    wishlist = serializers.IntegerField()  

    class Meta:
        model = WishlistitemModel
        fields = ["id", "wishlist", "product", "created_at", "updated_at", "deleted_at"]

    def validate_product(self, value):
        if not ProductModel.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Product with ID {value} does not exist.")
        return value  
    

    def validate_wishlist(self, value):
        if not WishlistModel.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Wishlist with ID {value} does not exist.")
        return value 

    def create(self, validated_data):
        product_id = validated_data.get("product")  
        wishlist_instance = validated_data.get("wishlist")  
        if isinstance(wishlist_instance, WishlistModel):  
            wishlist_id = wishlist_instance.id  
        else:
            wishlist_id = wishlist_instance 

        product_instance = ProductModel.objects.get(id=product_id)

        wishlist_instance = WishlistModel.objects.get(id=wishlist_id)

        wishlist_item = WishlistitemModel.objects.create(
            product=product_instance,
            wishlist=wishlist_instance
        )

        return wishlist_item
