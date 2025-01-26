from rest_framework import serializers

from ...models import StoreModel
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.address.serializers.country import ListCountrySerializer
from core.apps.address.serializers.state import ListStateSerializer
from core.apps.product.serializers.review import ListReviewSerializer


class BaseStoreSerializer(serializers.ModelSerializer):
    store_logo = ListImageSerializer(read_only=True)
    store_cover = ListImageSerializer(read_only=True)
    vendor = UserSerializer(read_only=True)
    country = ListCountrySerializer(read_only=True)
    state = ListStateSerializer(read_only=True)
    reviews = ListReviewSerializer(many=True)
    order_amount = serializers.FloatField()
    created_by_id = serializers.CharField()
    
    class Meta:
        model = StoreModel
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "city",
            "address",
            "pincode",
            "facebook",
            "twitter",
            "instagram",
            "youtube",
            "pinterest",
            "hide_vendor_email",
            "hide_vendor_phone",
            "created_by_id",
            "status",
            "is_approved",
            "created_at", 
            "updated_at",
            "deleted_at",
            "orders_count",
            "reviews_count",
            "products_count",
            "order_amount",
            "rating_count",
            "store_logo",
            "store_cover",
            "vendor",
            "country",
            "state",
            'reviews'
            # "product_images"
        ]

    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['hide_vendor_email'] = 1 if instance.hide_vendor_email else 0
        data['hide_vendor_phone'] = 1 if instance.hide_vendor_phone else 0
        data['status'] = 1 if instance.status else 0
        data['is_approved'] = 1 if instance.is_approved else 0
        return data


class ListStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta): ...


class RetrieveStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta): ...


class CreateStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta): ...
