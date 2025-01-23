from rest_framework import serializers

from ...models import PointsModel


class BasePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListPointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta): ...


class RetrievePointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta): ...


class CreatePointsSerializer(BasePointsSerializer):
    class Meta(BasePointsSerializer.Meta): ...
