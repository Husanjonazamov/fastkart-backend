from rest_framework import serializers

from ...models import CurrencyModel


class BaseCurrencySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
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


class ListCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...


class RetrieveCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...


class CreateCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...
