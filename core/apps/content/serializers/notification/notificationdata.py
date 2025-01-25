from rest_framework import serializers

from ...models import NotificationdataModel


class BaseNotificationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationdataModel
        exclude = [
            'id',
            "created_at",
            "updated_at",
        ]


class ListNotificationDataSerializer(BaseNotificationDataSerializer):
    class Meta(BaseNotificationDataSerializer.Meta): ...


class RetrieveNotificationDataSerializer(BaseNotificationDataSerializer):
    class Meta(BaseNotificationDataSerializer.Meta): ...


class CreateNotificationDataSerializer(BaseNotificationDataSerializer):
    class Meta(BaseNotificationDataSerializer.Meta): ...
