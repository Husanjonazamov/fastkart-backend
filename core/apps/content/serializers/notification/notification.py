from rest_framework import serializers
from ...models import NotificationModel, NotificationdataModel
from ..notification.notificationdata import ListNotificationDataSerializer


class BaseNotificationSerializer(serializers.ModelSerializer):
    data = ListNotificationDataSerializer()

    class Meta:
        model = NotificationModel
        fields = [
            "id",
            "type",
            "notifiable_type",
            "notifiable_id",  
            "data",
            "created_at",
            "updated_at"
        ]


class ListNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta):
        pass


class RetrieveNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta):
        pass


class CreateNotificationSerializer(BaseNotificationSerializer):
    notifiable_id = serializers.IntegerField(required=True) 

    class Meta(BaseNotificationSerializer.Meta):
        pass

    def create(self, validated_data):
        data = validated_data.pop('data')
        
        notification_data_instance = NotificationdataModel.objects.create(**data)

        notification_instance = NotificationModel.objects.create(data=notification_data_instance, **validated_data)

        return notification_instance
