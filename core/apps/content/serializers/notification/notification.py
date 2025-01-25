from rest_framework import serializers

from ...models import NotificationModel
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
    class Meta(BaseNotificationSerializer.Meta): ...


class RetrieveNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...


class CreateNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...
