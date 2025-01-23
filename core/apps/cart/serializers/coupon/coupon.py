from rest_framework import serializers

from ...models import CouponModel


class BaseCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta): ...


class RetrieveCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta): ...


class CreateCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta): ...
