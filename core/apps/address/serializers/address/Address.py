from rest_framework import serializers
from ...models import AddressModel
from ...models.country import CountryModel
from ...models.state import StateModel
from core.apps.accounts.models.user import User
from ..state.State import ListStateSerializer


class DisplayAddressCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ["id", "name"]


class BaseAddressSerializer(serializers.ModelSerializer):
    country = DisplayAddressCountrySerializer(read_only=True)
    country_id = serializers.IntegerField()
    state = ListStateSerializer(read_only=True)
    state_id = serializers.IntegerField()
    user_id = serializers.IntegerField(required=False)

    class Meta:
        model = AddressModel
        fields = [
            "id",
            "title",
            "user_id",
            "street",
            "city",
            "pincode",
            "is_default",
            "country_code",
            "phone",
            "country_id",
            "state_id",
            "country",
            "state",
        ]
        read_only_fields = [
            "id",
            "country",
            "state",
        ]

    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("There is no User with that id")
        return value

    def validate_state_id(self, value):
        try:
            state = StateModel.objects.select_related("country").get(id=value)
        except StateModel.DoesNotExist:
            raise serializers.ValidationError("There is no State with that id")

        country_id = self.initial_data.get("country_id") or self.validated_data.get("country_id")
        if not country_id:
            raise serializers.ValidationError("Country ID is required to validate State.")

        if state.country.id != int(country_id):
            raise serializers.ValidationError("State must be in the specified country.")

        return value


class ListAddressSerializer(BaseAddressSerializer):
    class Meta(BaseAddressSerializer.Meta):
        ...


class RetrieveAddressSerializer(BaseAddressSerializer):
    class Meta(BaseAddressSerializer.Meta):
        ...


class CreateAddressSerializer(BaseAddressSerializer):
    class Meta(BaseAddressSerializer.Meta):
        ...

    def create(self, validated_data):
        request = self.context.get("request")
        
        user_id = validated_data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found with the given id")
        
        validated_data["user"] = user

        country_id = validated_data.get('country_id')
        try:
            country = CountryModel.objects.get(id=country_id)
        except CountryModel.DoesNotExist:
            raise serializers.ValidationError("Country not found with the given id")
        
        validated_data["country"] = country

        state_id = validated_data.get('state_id')
        try:
            state = StateModel.objects.get(id=state_id)
        except StateModel.DoesNotExist:
            raise serializers.ValidationError("State not found with the given id")

        if state.country != country:
            raise serializers.ValidationError("State does not belong to the selected country.")
        
        validated_data["state"] = state

        return super().create(validated_data)
