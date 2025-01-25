from rest_framework import serializers

from ...models import OrderstatusModel

from rest_framework import serializers
from ...models import OrderstatusModel


class BaseOrderstatusSerializer(serializers.ModelSerializer):
    sequence = serializers.SerializerMethodField()
    created_by_id = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    system_reserve = serializers.SerializerMethodField()

    class Meta:
        model = OrderstatusModel
        fields = [
            "id",
            "name",
            "slug",
            "sequence",
            "created_by_id",
            "status",
            "system_reserve",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

    def get_sequence(self, obj):
        return str(obj.sequence)  

    def get_created_by_id(self, obj):
        return str(obj.created_by_id)  

    def get_status(self, obj):
        return int(obj.status) 

    def get_system_reserve(self, obj):
        return str(int(obj.system_reserve)) 


class ListOrderstatusSerializer(BaseOrderstatusSerializer):
    class Meta(BaseOrderstatusSerializer.Meta): ...


class RetrieveOrderstatusSerializer(BaseOrderstatusSerializer):
    class Meta(BaseOrderstatusSerializer.Meta): ...


class CreateOrderstatusSerializer(BaseOrderstatusSerializer):
    class Meta(BaseOrderstatusSerializer.Meta): ...
