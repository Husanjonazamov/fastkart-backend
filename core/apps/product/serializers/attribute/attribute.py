from rest_framework import serializers

from ...models import AttributeModel


class BaseAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta): ...


class RetrieveAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta): ...


class CreateAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta): ...
