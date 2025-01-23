from rest_framework import serializers

from ...models import TagsModel


class BaseTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListTagsSerializer(BaseTagsSerializer):
    class Meta(BaseTagsSerializer.Meta): ...


class RetrieveTagsSerializer(BaseTagsSerializer):
    class Meta(BaseTagsSerializer.Meta): ...


class CreateTagsSerializer(BaseTagsSerializer):
    class Meta(BaseTagsSerializer.Meta): ...
