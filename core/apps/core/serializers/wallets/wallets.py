from rest_framework import serializers
from ...models import WalletsModel, TransactionModel
from django.contrib.auth import get_user_model  


class BaseWalletsSerializer(serializers.ModelSerializer):
    consumer_id = serializers.IntegerField(write_only=True)
    transactions = serializers.ListField(child=serializers.IntegerField(), write_only=True)  

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
    class Meta(BaseWalletsSerializer.Meta):
        pass


class RetrieveWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta):
        pass


class CreateWalletsSerializer(BaseWalletsSerializer):
    class Meta(BaseWalletsSerializer.Meta):
        pass
