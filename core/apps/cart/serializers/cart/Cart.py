from rest_framework import serializers
from core.apps.accounts.models import User
from core.apps.product.serializers.product import ListProductSerializer
from core.apps.product.serializers.variation import ListVariationSerializer
from core.apps.product.models import ProductModel, VariationModel
from core.apps.cart.models import CartModel

class BaseCartSerializer(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    variation_id = serializers.SerializerMethodField()
    consumer_id = serializers.SerializerMethodField()
    product = ListProductSerializer(read_only=True)
    variation = ListVariationSerializer(read_only=True)

    class Meta:
        model = CartModel
        fields = [
            "id",
            "product_id",
            "variation_id",
            "consumer_id",
            "quantity",
            "sub_total",
            "created_at",
            "updated_at",
            "deleted_at",
            "product",
            "variation",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "deleted_at",
            "sub_total",
        ]
        
    def get_product_id(self, obj: CartModel) -> int | None:
        return obj.product.id if obj.product else None

    def get_variation_id(self, obj: CartModel) -> int | None:
        return obj.variation.id if obj.variation else None

    def get_consumer_id(self, obj: CartModel) -> int | None:
        return obj.consumer.id if obj.consumer else None


class ListCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta):
        fields = [
            "id",
            "product_id",
            "variation_id",
            "consumer_id",
            "quantity",
            "sub_total",
            "created_at",
            "updated_at",
            "deleted_at",
            "product",
            "variation",
        ]


class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta):
        fields = [
            "id",
            "product_id",
            "variation_id",
            "consumer_id",
            "quantity",
            "sub_total",
            "created_at",
            "updated_at",
            "deleted_at",
            "product",
            "variation",
        ]


class CreateCartSerializer(BaseCartSerializer):
    product_id = serializers.IntegerField()
    variation_id = serializers.IntegerField(required=False)
    consumer_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

    class Meta(BaseCartSerializer.Meta):
        fields = [
            "product_id",
            "variation_id",
            "consumer_id",
            "quantity",
        ]

    def validate(self, attrs):
        product_id = attrs.get("product_id")
        variation_id = attrs.get("variation_id")
        consumer_id = attrs.get("consumer_id")

        product = ProductModel.objects.filter(id=product_id).first()
        if not product:
            raise serializers.ValidationError({"product_id": "Product not found."})
        attrs["product"] = product

        variation = None
        if variation_id:
            variation = VariationModel.objects.filter(id=variation_id).first()
            if not variation:
                raise serializers.ValidationError({"variation_id": "Variation not found."})
        attrs["variation"] = variation

        consumer = User.objects.filter(id=consumer_id).first()
        if not consumer:
            raise serializers.ValidationError({"consumer_id": "Consumer not found."})
        attrs["consumer"] = consumer

        quantity = attrs.get("quantity", 1)
        if quantity < 1:
            raise serializers.ValidationError({"quantity": "Quantity must be at least 1."})

        return attrs

    def create(self, validated_data):
        product = validated_data.pop("product")
        variation = validated_data.pop("variation", None)
        consumer = validated_data.pop("consumer")
        quantity = validated_data.pop("quantity", 1)

        sub_total = product.sale_price * quantity

        cart = CartModel.objects.create(
            product=product,
            variation=variation,
            consumer=consumer,
            quantity=quantity,
            sub_total=sub_total,
        )
        return cart


class UpdateCartSerializer(BaseCartSerializer):
    product_id = serializers.IntegerField(required=False)
    variation_id = serializers.IntegerField(required=False)
    consumer_id = serializers.IntegerField(required=False)

    class Meta(BaseCartSerializer.Meta):
        fields = [
            "product_id",
            "variation_id",
            "consumer_id",
            "quantity",
        ]

    def update(self, instance: CartModel, validated_data):
        product_id = validated_data.pop("product_id", None)
        if product_id:
            try:
                product = ProductModel.objects.get(id=product_id)
                instance.product = product
            except ProductModel.DoesNotExist:
                raise serializers.ValidationError({"product_id": "Product not found."})
        
        variation_id = validated_data.pop("variation_id", None)
        if variation_id:
            try:
                variation = VariationModel.objects.get(id=variation_id)
                instance.variation = variation
            except VariationModel.DoesNotExist:
                raise serializers.ValidationError({"variation_id": "Variation not found."})

        consumer_id = validated_data.pop("consumer_id", None)
        if consumer_id:
            try:
                consumer = User.objects.get(id=consumer_id)
                instance.consumer = consumer
            except User.DoesNotExist:
                raise serializers.ValidationError({"consumer_id": "Consumer not found."})

        quantity = validated_data.pop("quantity", None)
        if quantity:
            instance.quantity = quantity
            instance.sub_total = instance.product.sale_price * quantity

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
