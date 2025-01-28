from rest_framework import serializers
from ...models import PointsModel
from core.apps.core.models.transaction import TransactionModel


class BasePointsSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(queryset=TransactionModel.objects.all(), many=True)
    consumer_id = serializers.IntegerField()
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = PointsModel
        fields = ['id', 'consumer_id', 'balance', 'transactions']


class ListPointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta):
        pass


class RetrievePointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta):
        pass


class CreatePointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta):
        pass

    def create(self, validated_data):
        transactions_data = validated_data.pop('transactions')
        
        consumer_id = validated_data['consumer_id']
        points, created = PointsModel.objects.get_or_create(
            consumer_id=consumer_id,
            defaults={'balance': validated_data['balance']}
        )

        if not created:
            points.balance = validated_data['balance']
            points.save()

        for transaction in transactions_data:
            points.transactions.add(transaction)

        return points
