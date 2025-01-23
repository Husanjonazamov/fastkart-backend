from rest_framework import serializers

from ...models import AddressModel


class BaseAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListAddressSerializer(BaseAddressSerializer):
    class Meta(BaseAddressSerializer.Meta): ...


class RetrieveAddressSerializer(BaseAddressSerializer):
    class Meta(BaseAddressSerializer.Meta): ...


class CreateAddressSerializer(BaseAddressSerializer):
    class Meta(BaseAddressSerializer.Meta): ...
