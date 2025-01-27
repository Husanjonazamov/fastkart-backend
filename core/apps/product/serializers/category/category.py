from rest_framework import serializers

from ...models import CategoryModel
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.content.models.image import ImageModel


class BaseCategorySerializer(serializers.ModelSerializer):
    category_image = ListImageSerializer()
    category_icon = ListImageSerializer()
    subcategories = serializers.SerializerMethodField()
    
    status = serializers.SerializerMethodField()

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

    def get_status(self, obj):
        return 1 if obj.status else 0

    def get_subcategories(self, obj):
        subcategories = obj.children.exclude(id=obj.pk)
        if subcategories.exists():
            return ListCategorySerializer(subcategories, many=True).data
        return None


class ListCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class RetrieveCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...



class CreateCategorySerializer(BaseCategorySerializer):
    parent_id = serializers.IntegerField(required=False)
    category_image = ListImageSerializer(required=False)
    category_icon = ListImageSerializer(required=False)

    class Meta(BaseCategorySerializer.Meta):
        pass

    def validate(self, attrs):
        """Custom validation if needed."""
        parent_id = attrs.get('parent_id')
        if parent_id:
            try:
                parent_category = CategoryModel.objects.get(id=parent_id)
                attrs['parent'] = parent_category
            except CategoryModel.DoesNotExist:
                raise serializers.ValidationError("Parent category does not exist.")
        return attrs

    def create(self, validated_data):
        category_image = validated_data.pop('category_image', None)
        category_icon = validated_data.pop('category_icon', None)
        
        request = self.context.get('request')
        if not request or not request.user:
            raise serializers.ValidationError("User is not authenticated.")

        category = CategoryModel.objects.create(created_by=request.user, **validated_data)

        if category_image:
            category.category_image = ImageModel.objects.create(**category_image)
        
        if category_icon:
            category.category_icon = ImageModel.objects.create(**category_icon)

        category.save()
        return category
