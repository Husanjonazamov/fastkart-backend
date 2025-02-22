from rest_framework import serializers
from ...models import OrderModel, OrderstatusModel
from core.apps.product.serializers.product import ListProductSerializer
from core.apps.orders.serializers.order.OrderStatus import ListOrderstatusSerializer
from core.apps.address.serializers.address import ListAddressSerializer
from core.apps.address.serializers.state import ListStateSerializer
from core.apps.accounts.serializers import UserSerializer
from core.apps.product.models import ProductModel
from core.apps.address.models import AddressModel





class BaseOrderSerializer(serializers.ModelSerializer):
    products = ListProductSerializer(many=True, read_only=True)
    order_status = ListOrderstatusSerializer(read_only=True)
    billing_address = ListAddressSerializer(read_only=True)
    shipping_address = ListAddressSerializer(read_only=True)
    store = ListStateSerializer(read_only=True)
    consumer = UserSerializer(read_only=True)
    sub_orders = serializers.SerializerMethodField()

    consumer_id = serializers.IntegerField(required=False)
    store_id = serializers.IntegerField(required=False)
    coupon_id = serializers.IntegerField(required=False)
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=OrderModel.objects.all(),
        required=False, 
        allow_null=True   
    )
    order_status_id = serializers.IntegerField(required=False)
    created_by_id = serializers.IntegerField(required=False)
    billing_address_id = serializers.IntegerField(required=False)
    shipping_address_id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "order_number",
            "consumer_id",
            "tax_total",
            "shipping_total",
            "points_amount",
            "wallet_balance",
            "amount",
            "total",
            "coupon_total_discount",
            "payment_method",
            "payment_status",
            'store_id',
            "billing_address_id",
            "shipping_address_id",
            "delivery_description",
            "delivery_interval",
            "order_status_id",
            "coupon_id",
            "parent_id",
            "created_by_id",
            "invoice_url",
            "status",
            "delivered_at",
            "created_at",
            "updated_at",
            "deleted_at",
            "store",
            "consumer",
            "products",
            "order_status",
            'sub_orders',
            "billing_address",
            "shipping_address",
        ]
        read_only_fields = [
            "id",
            "order_number",
            'delivered_at',
            "created_at",
            "updated_at",
            "deleted_at",
            "invoice_url",
            "store_id",
            "store",
            "consumer",
            "products",
            "order_status",
            'sub_orders',
            "billing_address",
            "shipping_address",
        ]

    def get_parent_id(self, obj):
        return obj.parent_id if obj.parent_id else None

    def get_sub_orders(self, obj):
        suborders = obj.sub_orders.exclude(id=obj.pk)  
        if suborders.exists():
            return ListOrderSerializer(suborders, many=True).data
        return []


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


