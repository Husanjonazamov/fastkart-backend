from rest_framework import serializers
from ...models import AttributeModel
from core.apps.accounts.models import User
from django.db import transaction
from ..attribute.attributeValue import ListAttributevalueSerializer as AttributevalueSerializers



class BaseAttributeSerializer(serializers.ModelSerializer):
    attribute_values = AttributevalueSerializers(many=True, required=False)

    class Meta:
        model = AttributeModel
        fields = [
            "id",
            "name",
            "style",
            "slug",
            "status",
            "created_by_id",
            "created_at",
            "updated_at",
            "deleted_at",
            "attribute_values", 
        ]


class ListAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = BaseAttributeSerializer.Meta.fields


class RetrieveAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = BaseAttributeSerializer.Meta.fields


class CreateAttributeSerializer(BaseAttributeSerializer):
    created_by_id = serializers.IntegerField(source="created_by.id", read_only=True)

    class Meta(BaseAttributeSerializer.Meta):
        fields = [
            "name",
            "style",
            "slug",
            "status",
            "created_by_id",
            "attribute_values",
        ]

    def create(self, validated_data):
        created_by_id = validated_data.pop("created_by_id", None)
        attribute_values = validated_data.pop("attribute_values", [])

        if created_by_id is None:
            created_by = self.context.get("request").user
        else:
            created_by = User.objects.get(id=created_by_id)

        if not isinstance(attribute_values, list):
            raise serializers.ValidationError(
                "'attribute_values' must be a list of attribute values."
            )

        with transaction.atomic():
            attribute = AttributeModel.objects.create(
                created_by=created_by, **validated_data
            )

            values = [
                AttributevalueSerializers(attribute=attribute, created_by=created_by, **value_data)
                for value_data in attribute_values
            ]

            AttributevalueSerializers.objects.bulk_create(values)

        return attribute

    def get_created_by_id(self, obj: User) -> int | None:
        return obj.created_by.id if obj.created_by else None
