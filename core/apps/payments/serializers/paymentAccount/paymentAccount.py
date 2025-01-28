from rest_framework import serializers
from ...models import PaymentaccountModel
from core.apps.accounts.models.user import User

class BasePaymentaccountSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()
    is_default = serializers.BooleanField()

    class Meta:
        model = PaymentaccountModel
        fields = [
            "id",
            "user",
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
    class Meta(BasePaymentaccountSerializer.Meta):
        pass


class RetrievePaymentaccountSerializer(BasePaymentaccountSerializer):
    class Meta(BasePaymentaccountSerializer.Meta):
        pass


class CreatePaymentaccountSerializer(BasePaymentaccountSerializer):
    user_id = serializers.IntegerField()  

    class Meta(BasePaymentaccountSerializer.Meta):
        fields = [
            "user_id", 
            "paypal_email",
            "bank_name",
            "bank_holder_name",
            "bank_account_no",
            "swift",
            "ifsc",
            "is_default",
            "status",
        ]

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        user = User.objects.filter(id=user_id).first()  
        if not user:
            raise serializers.ValidationError({"user_id": "Foydalanuvchi topilmadi."})
        attrs["user"] = user 

        is_default = attrs.get('is_default', False)
        attrs['is_default'] = is_default if is_default else False

        return attrs

    def create(self, validated_data):
        user = validated_data.pop('user')  
        
        payment_account = PaymentaccountModel.objects.filter(user=user).first()
        if payment_account:
            for key, value in validated_data.items():
                setattr(payment_account, key, value)
            payment_account.save()
            return payment_account
        else:
            payment_account = PaymentaccountModel.objects.create(user=user, **validated_data)
            return payment_account
