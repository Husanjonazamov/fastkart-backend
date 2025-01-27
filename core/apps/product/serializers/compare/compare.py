from rest_framework import serializers
from ...models import CompareModel, ProductModel
from ...serializers.compare.compareItem import ListCompareitemSerializer
from core.apps.accounts.models import User

class BaseCompareSerializer(serializers.ModelSerializer):
    compare_items = ListCompareitemSerializer(many=True, read_only=True)

    class Meta:
        model = CompareModel
        fields = [
            "id", 
            "consumer", 
            "total", 
            "created_at",  
            "updated_at", 
            "compare_items"
        ]


class ListCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta):
        pass


class RetrieveCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta):
        pass


class CreateCompareSerializer(BaseCompareSerializer):
    consumer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    products = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all(), many=True, write_only=True)

    class Meta(BaseCompareSerializer.Meta):
        fields = BaseCompareSerializer.Meta.fields + ["consumer", "products"]

    def create(self, validated_data):
        consumer = validated_data.get('consumer')
        products = validated_data.pop('products', [])
        
        compare, created = CompareModel.objects.get_or_create(
            consumer=consumer, defaults=validated_data
        )

        for product in products:
            compare.compare_items.create(product=product)

        compare.save()
        return compare
    



class CompareUpdateSerializer(BaseCompareSerializer):
    consumer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    products = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all(), many=True, write_only=True, required=False)

    class Meta:
        model = CompareModel
        fields = ["consumer", "products"]

    def update(self, instance, validated_data):
        consumer = validated_data.get('consumer')
        if consumer:
            instance.consumer = consumer

        products = validated_data.get('products', [])
        if products:
            instance.compare_items.set(products)

        instance.save()
        return instance
