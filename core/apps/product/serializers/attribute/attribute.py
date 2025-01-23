from rest_framework import serializers
from ...models import AttributeModel
from ..attribute.attributeValue import ListAttributevalueSerializer


class BaseAttributeSerializer(serializers.ModelSerializer):
    attribute_value = ListAttributevalueSerializer(many=True, read_only=True)  

    class Meta:
        model = AttributeModel
        fields = [
            "id",
            "name",
            "style",
            "slug",
            "status",
            "created_by",
            "created_at",
            "updated_at",
            "deleted_at",
            "attribute_value",  
        ]


class ListAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = BaseAttributeSerializer.Meta.fields


class RetrieveAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = BaseAttributeSerializer.Meta.fields


class CreateAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = [
            "name",
            "style",
            "slug",
            "status",
            "created_by",
        ]
