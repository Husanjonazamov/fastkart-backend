from rest_framework import serializers

from ...models import RefundModel
from core.apps.product.serializers.store import ListStoreSerializer
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.orders.serializers.order import ListOrderSerializer



class BaseRefundSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(required=False)
    store_id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField(required=False)
    consumer_id = serializers.IntegerField(required=False)
    variation_id = serializers.IntegerField(required=False)
    refund_image_id = serializers.IntegerField(required=False)
    
    user = UserSerializer(source="consumer", required=False)
    store = ListStoreSerializer(required=False)
    order = ListOrderSerializer(required=False)
    refund_image = ListImageSerializer(required=False)
    
    
    class Meta: 
        model = RefundModel
        fields = [
            "id",
            "reason",
            "amount",
            "quantity",
            "store_id",
            "order_id",
            "product_id",
            "consumer_id",
            "variation_id",
            "refund_image_id",
            "payment_type",
            "status",
            "is_used",
            "created_at",
            "updated_at",
            "deleted_at",
            "user",
            'store',
            'order',
            'refund_image'
        ]
        
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "deleted_at",
        ]


class ListRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...


class RetrieveRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...


class CreateRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...
