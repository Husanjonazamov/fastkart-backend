from rest_framework import serializers

from ...models import PaymentaccountModel


class BasePaymentaccountSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()
    is_default = serializers.BooleanField()

    
    
    class Meta:
        model = PaymentaccountModel

        fields = [
            "id",
            "user_id",
            "paypal_email",
            "bank_name",
            "bank_holder_name",
            "bank_account_no",
            "swift",
            "ifsc",
            "is_default",
            "status",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['is_default'] = "1" if representation.get('is_default', False) else "0"
        return representation


class ListPaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta): ...


class RetrievePaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta): ...


class CreatePaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta): ...
