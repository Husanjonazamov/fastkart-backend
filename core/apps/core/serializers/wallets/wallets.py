from rest_framework import serializers

from ...models import WalletsModel
from ..transaction import ListTransactionSerializer


class BaseWalletsSerializer(serializers.ModelSerializer):
    consumer_id = serializers.IntegerField(source='consumer.id', read_only=True)
    transactions = ListTransactionSerializer(many=True, read_only=True)
    
    class Meta:
        model = WalletsModel
        fields = [
            'id',
            'consumer_id',
            'type',
            'balance',
            'transactions'
        ]


class ListWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta): ...


class RetrieveWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta): ...


class CreateWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta): ...
