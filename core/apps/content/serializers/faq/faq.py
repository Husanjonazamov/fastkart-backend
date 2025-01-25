from rest_framework import serializers

from ...models import FaqModel


class BaseFaqSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = FaqModel
        fields = [
            "id",
            "title",
            "description",
            "created_by_id",
            "status", 
            "created_at",
            "updated_at",
            "deleted_at",
        ]
    
    def get_status(self, obj):
        return 1 if obj.status else 0


class ListFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class RetrieveFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class CreateFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...
