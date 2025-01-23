from rest_framework import serializers

from ...models import NotificationModel


class BaseNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...


class RetrieveNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...


class CreateNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...
