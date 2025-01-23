from rest_framework import serializers

from ...models import VariationModel


class BaseVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariationModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListVariationSerializer(BaseVariationSerializer):
    class Meta(BaseVariationSerializer.Meta): ...


class RetrieveVariationSerializer(BaseVariationSerializer):
    class Meta(BaseVariationSerializer.Meta): ...


class CreateVariationSerializer(BaseVariationSerializer):
    class Meta(BaseVariationSerializer.Meta): ...
