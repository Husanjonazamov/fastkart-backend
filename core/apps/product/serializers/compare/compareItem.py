from rest_framework import serializers

from ...models import CompareitemModel


class BaseCompareitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareitemModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCompareitemSerializer(BaseCompareitemSerializer):
    class Meta(BaseCompareitemSerializer.Meta): ...


class RetrieveCompareitemSerializer(BaseCompareitemSerializer):
    class Meta(BaseCompareitemSerializer.Meta): ...


class CreateCompareitemSerializer(BaseCompareitemSerializer):
    class Meta(BaseCompareitemSerializer.Meta): ...
