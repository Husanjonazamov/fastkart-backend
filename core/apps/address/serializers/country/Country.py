from rest_framework import serializers

from ...models import CountryModel
from ..state.State import ListStateSerializer


class BaseCountrySerializer(serializers.ModelSerializer):
    states = ListStateSerializer(many=True)
    
    class Meta:
        model = CountryModel
        fields = [
            'id',
            'name',
            'currency',
            'currency_symbol',
            'iso_3166_2',
            'iso_3166_3',
            'calling_code',
            'flag',
            'states'
        ]


class ListCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class RetrieveCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class CreateCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...
