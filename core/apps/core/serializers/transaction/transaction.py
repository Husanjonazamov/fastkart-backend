from rest_framework import serializers

from ...models import TransactionModel


class BaseTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta): ...


class RetrieveTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta): ...


class CreateTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta): ...
