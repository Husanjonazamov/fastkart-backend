from rest_framework import serializers

from ...models import TagsModel


class BaseTagsSerializer(serializers.ModelSerializer):
    created_by_id = serializers.SerializerMethodField(required=False)

    class Meta:
        model = TagsModel
        fields = [
            'id',
            'name',
            'slug',
            'type',
            'descriptions',
            'created_by_id',
            'status',
            'created_at',
            'updated_at',
            'deleted_at',
            'blogs_count',
            'products_count',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_by',
            'created_at',
            'updated_at',
            'deleted_at',
            'blogs_count',
            'products_count',
        ]
        
    def get_created_by_id(self, obj: TagsModel) -> int | None:
        return obj.created_by.id if obj.created_by else None


class ListTagsSerializer(BaseTagsSerializer):
    class Meta(BaseTagsSerializer.Meta): ...


class RetrieveTagsSerializer(BaseTagsSerializer):
    class Meta(BaseTagsSerializer.Meta): ...


class CreateTagsSerializer(BaseTagsSerializer):
    class Meta(BaseTagsSerializer.Meta):
        fields = BaseTagsSerializer.Meta.fields    
    
    def create(self, validated_data):
        user = self.context.get('request').user 
        validated_data['created_by'] = user 

        tag = TagsModel.objects.create(**validated_data)
        
        return tag

