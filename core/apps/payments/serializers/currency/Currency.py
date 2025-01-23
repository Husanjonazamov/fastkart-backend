from rest_framework import serializers

from ...models import CurrencyModel


class BaseCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...


class RetrieveCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...


class CreateCurrencySerializer(BaseCurrencySerializer):
    class Meta(BaseCurrencySerializer.Meta): ...
