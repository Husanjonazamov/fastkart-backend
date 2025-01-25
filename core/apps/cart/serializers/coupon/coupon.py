from rest_framework import serializers

from ...models import CouponModel


class BaseCouponSerializer(serializers.ModelSerializer):
    created_by_id = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    is_expired = serializers.SerializerMethodField()
    is_apply_all = serializers.SerializerMethodField()
    is_first_order = serializers.SerializerMethodField()
    
    class Meta:
        model = CouponModel
        fields = [
            "id",
            "title",
            "description",
            "code",
            "type",
            "amount",
            "min_spend",
            "is_unlimited",
            "usage_per_coupon",
            "usage_per_customer",
            "used",
            "status",
            "is_expired",
            "is_apply_all",
            "is_first_order",
            "start_date",
            "end_date",
            "created_by_id",
            "created_at",
            "updated_at",
            "deleted_at"
        ]
        
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

        
    def get_status(self, obj):
        return 1 if obj.status else 0

    def get_is_expired(self, obj):
        return 1 if obj.is_expired else 0

    def get_is_apply_all(self, obj):
        return 1 if obj.is_apply_all else 0

    def get_is_first_order(self, obj):
        return 1 if obj.is_first_order else 0
    
    
    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)

    def get_created_by_id(self, obj: CouponModel) -> int | None:
        return obj.created_by.id if obj.created_by else None


class ListCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta): ...


class RetrieveCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta): ...


class CreateCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta): ...
