from rest_framework import serializers

from ...models import CompareModel
from ...serializers.compare.compareItem import ListCompareitemSerializer


class BaseCompareSerializer(serializers.ModelSerializer):
    compare_items = ListCompareitemSerializer(many=True)
    
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
    class Meta(BaseCompareSerializer.Meta): ...


class RetrieveCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta): ...


class CreateCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta): ...



class CompareUpdateSerializer(BaseCompareSerializer):
    products = serializers.ListField()

    class Meta:
        model = CompareModel
        fields = ["consumer", "products"]
    
    def update(self, instance, validated_data):
        consumer_id = validated_data.get('consumer')
        if consumer_id:
            instance.consumer_id = consumer_id

        products = validated_data.get('products', [])
        if products:
            instance.compare_items.set(products)  

        instance.save()

        return instance