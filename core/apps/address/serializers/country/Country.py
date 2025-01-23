from rest_framework import serializers

from ...models import CountryModel


class BaseCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class RetrieveCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class CreateCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...
