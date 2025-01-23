from rest_framework import serializers

from ...models import AttributevalueModel


class BaseAttributevalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributevalueModel
        fields = [
            "id",
            "value",
            "slug",
            "hex_color",
            "created_by",
            "created_at",
            "updated_at",
            "deleted_at",
        ]


class ListAttributevalueSerializer(BaseAttributevalueSerializer):
    class Meta(BaseAttributevalueSerializer.Meta):
        fields = BaseAttributevalueSerializer.Meta.fields


class RetrieveAttributevalueSerializer(BaseAttributevalueSerializer):
    class Meta(BaseAttributevalueSerializer.Meta):
        fields = BaseAttributevalueSerializer.Meta.fields


class CreateAttributevalueSerializer(BaseAttributevalueSerializer):
    class Meta(BaseAttributevalueSerializer.Meta):
        fields = [
            "value",
            "slug",
            "hex_color",
            "attribute",
            "created_by",
        ]
