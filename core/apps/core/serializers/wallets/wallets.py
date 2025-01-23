from rest_framework import serializers

from ...models import WalletsModel


class BaseWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta): ...


class RetrieveWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta): ...


class CreateWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta): ...
