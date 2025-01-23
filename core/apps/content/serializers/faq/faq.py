from rest_framework import serializers

from ...models import FaqModel


class BaseFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class RetrieveFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class CreateFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...
