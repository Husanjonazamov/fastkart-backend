from rest_framework import serializers

from ...models.image import ImageModel


class BaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = [
            "id",
            "collection_name",
            "name",
            "file_name",
            "mime_type",
            "disk",
            "conversions_disk",
            "size",
            "created_by",
            "created_at",
            "updated_at",
            "original_url",
        ]


class ListImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta): ...


class RetrieveImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta): ...


class CreateImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta): ...
