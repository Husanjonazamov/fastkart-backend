from rest_framework import serializers

from ...models import CategoryModel
from core.apps.content.serializers.image import ListImageSerializer


class BaseCategorySerializer(serializers.ModelSerializer):
    category_image = ListImageSerializer()
    category_icon = ListImageSerializer()
    subcategories = serializers.SerializerMethodField()
    
    
    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "name",
            "description",
            "status",
            "type",
            "commission_rate",
            "created_by_id",
            "category_image_id",
            "category_icon_id",
            "parent_id",
            "category_image",
            "category_icon",
            "subcategories",
        ]


    def get_created_by_id(self, obj):
        return obj.created_by.id if obj.created_by else None

    def get_category_image_id(self, obj):
        return obj.category_image.id if obj.category_image else None

    def get_category_icon_id(self, obj):
        return obj.category_icon.id if obj.category_icon else None

    def get_parent_id(self, obj):
        return obj.parent.id if obj.parent else None

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        if subcategories.exists():
            print('category list')
            return ListCategorySerializer(subcategories, many=True).data
        return None
    
    

class ListCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class RetrieveCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class CreateCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...
