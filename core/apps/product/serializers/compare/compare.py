from rest_framework import serializers

from ...models import CompareModel


class BaseCompareSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta): ...


class RetrieveCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta): ...


class CreateCompareSerializer(BaseCompareSerializer):
    class Meta(BaseCompareSerializer.Meta): ...
