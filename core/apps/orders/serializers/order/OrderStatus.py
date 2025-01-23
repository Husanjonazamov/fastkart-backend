from rest_framework import serializers

from ...models import OrderstatusModel


class BaseOrderstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderstatusModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListOrderstatusSerializer(BaseOrderstatusSerializer):
    class Meta(BaseOrderstatusSerializer.Meta): ...


class RetrieveOrderstatusSerializer(BaseOrderstatusSerializer):
    class Meta(BaseOrderstatusSerializer.Meta): ...


class CreateOrderstatusSerializer(BaseOrderstatusSerializer):
    class Meta(BaseOrderstatusSerializer.Meta): ...
