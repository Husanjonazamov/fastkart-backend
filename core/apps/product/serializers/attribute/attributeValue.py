from rest_framework import serializers

from ...models import AttributevalueModel


class BaseAttributevalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributevalueModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListAttributevalueSerializer(BaseAttributevalueSerializer):
    class Meta(BaseAttributevalueSerializer.Meta): ...


class RetrieveAttributevalueSerializer(BaseAttributevalueSerializer):
    class Meta(BaseAttributevalueSerializer.Meta): ...


class CreateAttributevalueSerializer(BaseAttributevalueSerializer):
    class Meta(BaseAttributevalueSerializer.Meta): ...
