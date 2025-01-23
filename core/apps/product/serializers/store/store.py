from rest_framework import serializers

from ...models import StoreModel


class BaseStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta): ...


class RetrieveStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta): ...


class CreateStoreSerializer(BaseStoreSerializer):
    class Meta(BaseStoreSerializer.Meta): ...
