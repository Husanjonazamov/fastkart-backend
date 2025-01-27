from rest_framework import serializers

from ...models import CountryModel
from ..state.State import ListStateSerializer
from core.apps.address.models.state import StateModel

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


class CreateCountrySerializer(serializers.ModelSerializer):
    states_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)

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
            'states_ids'
        ]

    def create(self, validated_data):
        states_ids = validated_data.pop('states_ids', [])

        country = CountryModel.objects.create(**validated_data)

        for state_id in states_ids:
            try:
                state = StateModel.objects.get(id=state_id) 
                state.country = country
                state.save()
            except StateModel.DoesNotExist:
                raise serializers.ValidationError(f"State with ID {state_id} does not exist.")

        return country