from rest_framework import serializers

from ...models import AttributevalueModel
from core.apps.accounts.models import User


class BaseAttributevalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributevalueModel
        fields = [
            "id",
            "value",
            "slug",
            "hex_color",
            "attribute_id", 
            "created_by_id",
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
    created_by_id = serializers.SerializerMethodField()

    class Meta(BaseAttributevalueSerializer.Meta):
        fields = [
            "value",
            "slug",
            "hex_color",
            "attribute", 
            "created_by",
        ]

    def create(self, validated_data):
        created_by_id = validated_data.pop("created_by_id", None)

        if created_by_id is None:
            created_by_id = self.context.get("request").user.id

        validated_data["created_by_id"] = created_by_id
        return super().create(validated_data)

    def get_created_by_id(self, obj: User) -> int | None:
        return obj.created_by.id if obj.created_by else None
