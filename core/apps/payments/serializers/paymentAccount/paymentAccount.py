from rest_framework import serializers

from ...models import PaymentaccountModel


class BasePaymentaccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentaccountModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListPaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta): ...


class RetrievePaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta): ...


class CreatePaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta): ...
