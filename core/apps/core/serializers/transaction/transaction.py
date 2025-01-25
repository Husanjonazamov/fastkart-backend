from rest_framework import serializers

from ...models import TransactionModel


class BaseTransactionSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(required=False)
    point_id = serializers.IntegerField(required=False)
    wallet_id = serializers.IntegerField(required=False)
    type = serializers.CharField(max_length=10, required=False, allow_null=True)
    amount = serializers.IntegerField()
    from_user = serializers.IntegerField()
    
    class Meta:
        model = TransactionModel
        fields = [
            'id',
            'wallet_id',
            'order_id',
            'point_id',
            'amount',
            'type',
            'detail',
            'from_user',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'from_user',
            'created_at',
        ]
        
        
    def create(self, validated_data):
        print(validated_data)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['from_user'] = request.user.id
        
        return TransactionModel.objects.create(**validated_data)


class ListTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta): ...


class RetrieveTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta): ...


class CreateTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta): ...
