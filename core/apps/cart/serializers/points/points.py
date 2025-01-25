from rest_framework import serializers

from ...models import PointsModel
from core.apps.core.serializers.transaction import ListTransactionSerializer


class BasePointsSerializer(serializers.ModelSerializer):
    transactions = ListTransactionSerializer(many=True)
    consumer_id = serializers.IntegerField()
    balance = serializers.CharField()
    class Meta:
        model = PointsModel
        fields = [
            'id',
            'consumer_id',
            'balance',
            'transactions'
        ]


class ListPointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta): ...


class RetrievePointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta): ...


class CreatePointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta): ...
