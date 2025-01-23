from rest_framework import serializers

from ...models import CartModel


class BaseCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class CreateCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...
