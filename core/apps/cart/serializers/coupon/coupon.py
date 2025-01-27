from rest_framework import serializers
from ...models import CouponModel
from core.apps.accounts.models.user import User




class BaseCouponSerializer(serializers.ModelSerializer):
    created_by_id = serializers.IntegerField(source="created_by.id", read_only=True)  
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

    def get_created_by_id(self, obj: CouponModel) -> int | None:
        return obj.created_by.id if obj.created_by else None

class ListCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta):
        pass


class RetrieveCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta):
        pass


class CreateCouponSerializer(BaseCouponSerializer):
    class Meta(BaseCouponSerializer.Meta):
        pass

    def validate_code(self, value):
        """
        Validatsiya uchun: Agar kod allaqachon mavjud bo'lsa, xatolik yuboriladi
        """
        if CouponModel.objects.filter(code=value).exists():
            raise serializers.ValidationError("This coupon code already exists.")
        return value
    
    def create(self, validated_data):
        user = self.context["request"].user

        if user.is_authenticated:
            validated_data["created_by"] = user
        else:
            raise serializers.ValidationError("Foydalanuvchi avtorizatsiya qilinmagan.")

        return super().create(validated_data)

    
