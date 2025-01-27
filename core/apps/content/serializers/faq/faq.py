from rest_framework import serializers
from ...models import FaqModel
from core.apps.accounts.models.user import User


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
    created_by_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta(BaseFaqSerializer.Meta):
        fields = BaseFaqSerializer.Meta.fields  

    def create(self, validated_data):
        created_by = validated_data.pop('created_by_id') 
        faq_instance = FaqModel.objects.create(created_by=created_by, **validated_data)
        return faq_instance
