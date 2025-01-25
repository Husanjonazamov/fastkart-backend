from rest_framework import serializers

from ...models import StateModel


class BaseStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        fields = [
            'id',
            'name',
            'country',
            'created_at',
            'updated_at',
        ]
        
class ListStateSerializer(BaseStateSerializer):
    class Meta(BaseStateSerializer.Meta): ...


class RetrieveStateSerializer(BaseStateSerializer):
    class Meta(BaseStateSerializer.Meta): ...


class CreateStateSerializer(BaseStateSerializer):
    class Meta(BaseStateSerializer.Meta): ...
