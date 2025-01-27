from rest_framework import serializers
from ...models import AttributeModel, AttributevalueModel
from core.apps.accounts.models import User
from django.db import transaction
from ..attribute.attributeValue import ListAttributevalueSerializer as AttributevalueSerializers


class BaseAttributeSerializer(serializers.ModelSerializer):
    attribute_values = AttributevalueSerializers(many=True, required=False)
    status = serializers.SerializerMethodField()

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

    def get_status(self, obj: AttributeModel):
        return 1 if obj.status else 0


class ListAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = BaseAttributeSerializer.Meta.fields


class RetrieveAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = BaseAttributeSerializer.Meta.fields

class CreateAttributeSerializer(BaseAttributeSerializer):
    # Instead of receiving full attribute value data, we receive a list of ids
    attribute_values_ids = serializers.ListField(
        child=serializers.IntegerField(), required=False
    )

    class Meta(BaseAttributeSerializer.Meta):
        fields = [
            "name",
            "style",
            "slug",
            "status",
            "attribute_values_ids",  # We will now use the ids for the attribute values
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        created_by = request.user if request.user.is_authenticated else None

        if not created_by:
            raise serializers.ValidationError("User must be authenticated.")

        attribute_values_ids = validated_data.pop("attribute_values_ids", [])

        if not isinstance(attribute_values_ids, list):
            raise serializers.ValidationError(
                "'attribute_values_ids' must be a list of attribute value IDs."
            )

        with transaction.atomic():
            # Create the main attribute model
            attribute = AttributeModel.objects.create(
                created_by=created_by, **validated_data
            )

            # If attribute_values_ids is provided, link the attribute value instances
            if attribute_values_ids:
                # Fetch AttributevalueModel objects based on ids
                values = []
                for value_id in attribute_values_ids:
                    try:
                        attribute_value = AttributevalueModel.objects.get(id=value_id)
                    except AttributevalueModel.DoesNotExist:
                        raise serializers.ValidationError(
                            f"Attribute value with ID {value_id} does not exist."
                        )
                    
                    # Add a link between the created attribute and the existing attribute value
                    attribute_value.attribute = attribute
                    attribute_value.save()

                return attribute

        return attribute
    
class UpdateAttributeSerializer(BaseAttributeSerializer):
    class Meta(BaseAttributeSerializer.Meta):
        fields = [
            "id",
            "name",
            "style",
            "slug",
            "status",
            "attribute_values",
        ]

    def update(self, instance, validated_data):
        attribute_values = validated_data.pop("attribute_values", [])

        if not isinstance(attribute_values, list):
            raise serializers.ValidationError(
                "'attribute_values' must be a list of attribute values."
            )

        instance.name = validated_data.get('name', instance.name)
        instance.style = validated_data.get('style', instance.style)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if attribute_values:
            instance.attribute_values.all().delete()

            values = [
                AttributevalueSerializers(attribute=instance, **value_data)
                for value_data in attribute_values
            ]

            AttributevalueSerializers.objects.bulk_create(values)

        return instance


class DeleteAttributeSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def delete(self):
        attribute_id = self.validated_data.get('id')
        try:
            attribute = AttributeModel.objects.get(id=attribute_id)
        except AttributeModel.DoesNotExist:
            raise serializers.ValidationError("Attribute not found.")

        attribute.attribute_values.all().delete()

        attribute.delete()

        return {"message": "Attribute and its values have been deleted successfully."}
