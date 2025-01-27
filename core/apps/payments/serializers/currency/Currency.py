from rest_framework import serializers
from ...models import CurrencyModel
from django.contrib.auth.models import User



class BaseCurrencySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    created_by_id = serializers.SerializerMethodField()

    class Meta:
        model = CurrencyModel
        fields = [
            "id", 
            "code", 
            "symbol", 
            "no_of_decimal", 
            "exchange_rate", 
            "symbol_position", 
            "thousands_separator", 
            "decimal_separator", 
            "system_reserve", 
            "status", 
            "created_by_id", 
            "created_at", 
            "updated_at", 
            "deleted_at"
        ]
        
    def get_status(self, obj):
        return 1 if obj.status else 0

    def get_created_by_id(self, obj: CurrencyModel) -> int | None:
        return obj.created_by.id if obj.created_by else None


class ListCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...


class RetrieveCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...


class CreateCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta):
        read_only_fields = [
            "id", "created_at", "updated_at", "deleted_at"
        ]

    def create(self, validated_data):
        user = self.context["request"].user  
        validated_data["created_by"] = user  
        return super().create(validated_data)

