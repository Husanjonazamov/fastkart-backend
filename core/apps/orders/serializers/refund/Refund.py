from rest_framework import serializers

from ...models import RefundModel


class BaseRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefundModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...


class RetrieveRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...


class CreateRefundSerializer(BaseRefundSerializer):
    class Meta(BaseRefundSerializer.Meta): ...
