from rest_framework import serializers

from ...models import RefundModel
from core.apps.product.serializers.store import ListStoreSerializer
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.orders.serializers.order import ListOrderSerializer
from core.apps.product.models import ProductModel, StoreModel, VariationModel
from core.apps.accounts.models.user import User
from core.apps.content.models import ImageModel
from core.apps.orders.models import OrderModel




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
    amount = serializers.FloatField()
    
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
        
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if "is_used" in data:
            data["is_used"] = "1" if instance.is_used else "0"
        return data


class ListRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...


class RetrieveRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...


class CreateRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta):
        pass
    
    def validate(self, attrs):
        store_id = attrs.get('store_id')
        order_id = attrs.get('order_id')
        product_id = attrs.get('product_id')
        consumer_id = attrs.get('consumer_id')
        variation_id = attrs.get('variation_id')
        refund_image_id = attrs.get('refund_image_id')

        store = StoreModel.objects.filter(id=store_id).first()
        if not store:
            raise serializers.ValidationError({"store_id": "Store not found."})
        attrs['store'] = store
        order = OrderModel.objects.filter(id=order_id).first()
        
        if not order:
            raise serializers.ValidationError({"order_id": "Order not found."})
        attrs['order'] = order

        product = ProductModel.objects.filter(id=product_id).first()
        if not product:
            raise serializers.ValidationError({"product_id": "Product not found."})
        attrs['product'] = product

        consumer = User.objects.filter(id=consumer_id).first()
        if not consumer:
            raise serializers.ValidationError({"consumer_id": "Consumer not found."})
        attrs['consumer'] = consumer

        variation = None
        if variation_id:
            variation = VariationModel.objects.filter(id=variation_id).first()
            if not variation:
                raise serializers.ValidationError({"variation_id": "Variation not found."})
        attrs['variation'] = variation

        refund_image = None
        if refund_image_id:
            refund_image = ImageModel.objects.filter(id=refund_image_id).first()
            if not refund_image:
                raise serializers.ValidationError({"refund_image_id": "Refund image not found."})
        attrs['refund_image'] = refund_image

        return attrs

    def create(self, validated_data):
        store = validated_data.pop('store')
        order = validated_data.pop('order')
        product = validated_data.pop('product')
        consumer = validated_data.pop('consumer')
        variation = validated_data.pop('variation', None)
        refund_image = validated_data.pop('refund_image', None)

        refund = RefundModel.objects.create(
            reason=validated_data.get('reason'),
            amount=validated_data.get('amount'),
            quantity=validated_data.get('quantity'),
            store=store,
            order=order,
            product=product,
            consumer=consumer,
            variation=variation,
            refund_image=refund_image,
            payment_type=validated_data.get('payment_type'),
            status=validated_data.get('status'),
            is_used=validated_data.get('is_used', False)  
        )

        return refund
