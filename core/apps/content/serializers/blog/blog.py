from rest_framework import serializers

from ...models import BlogModel


class BaseBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...


class RetrieveBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...


class CreateBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...
