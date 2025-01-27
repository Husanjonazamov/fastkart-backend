from django.contrib.auth import get_user_model
from rest_framework import serializers
import importlib
from core.apps.accounts.models import Role, User

def dynamic_import(import_path):
    module_path, class_name = import_path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)



ListWalletsSerializer = dynamic_import("core.apps.core.serializers.wallets.ListWalletsSerializer")
ListAddressSerializer = dynamic_import("core.apps.address.serializers.address.ListAddressSerializer")
ListPaymentaccountSerializer = dynamic_import("core.apps.payments.serializers.paymentAccount.ListPaymentaccountSerializer")




class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'guard_name',
            'system_reserve',
            'created_at',
            'updated_at',
            'pivot'
        ]

class UserSerializer(serializers.ModelSerializer):
    profile_image_id = serializers.SerializerMethodField(required=False)
    created_by_id = serializers.SerializerMethodField(required=False)

    role = RoleSerializers()
    wallet = ListWalletsSerializer()
    address = ListAddressSerializer(many=True)
    vendor_wallet = ListWalletsSerializer()
    payment_account = ListPaymentaccountSerializer()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "name",
            "email",
            "country_code",
            "phone",
            "profile_image_id",
            "system_reserve",
            "status",
            "created_by_id",
            "email_verified_at",
            "created_at",
            "updated_at",
            "deleted_at",
            "orders_count",
            "role",
            "wallet",
            'address',
            "vendor_wallet",
            'payment_account',
        ]
        read_only_fields = [
            "id",
            "profile_image_id",
            "created_at",
            "updated_at",
            "deleted_at",
            "orders_count",
            "email_verified_at",
        ]

    def get_profile_image_id(self, obj: User) -> int | None:
        return obj.profile_image.id if obj.profile_image else None

    def get_created_by_id(self, obj: User) -> int | None:
        return obj.created_by.id if obj.created_by else None

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name"
        ]
