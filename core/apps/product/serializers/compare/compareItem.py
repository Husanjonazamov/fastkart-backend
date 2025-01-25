from rest_framework import serializers

from ...models import CompareitemModel
from core.apps.product.serializers.product import ListProductSerializer



class BaseCompareitemSerializer(serializers.ModelSerializer):
    product = ListProductSerializer()
    class Meta:
        model = CompareitemModel
        fields = [
            "product",
            "created_at",
            "updated_at",
            "deleted_at",
        ]


class ListCompareitemSerializer(BaseCompareitemSerializer):
    class Meta(BaseCompareitemSerializer.Meta): ...


class RetrieveCompareitemSerializer(BaseCompareitemSerializer):
    class Meta(BaseCompareitemSerializer.Meta): ...


class CreateCompareitemSerializer(BaseCompareitemSerializer):
    class Meta(BaseCompareitemSerializer.Meta): ...
