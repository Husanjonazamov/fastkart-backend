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
            "slug",
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



class CreateCategorySerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(required=False)
    category_image_id = serializers.IntegerField(required=False)
    category_icon_id = serializers.IntegerField(required=False)

    class Meta:
        model = CategoryModel
        fields = [
            "name",
            "slug",
            "description",
            "status",
            "type",
            "commission_rate",
            "parent_id",
            "category_image_id",
            "category_icon_id",
        ]

    def validate(self, attrs):
        parent_id = attrs.get('parent_id')
        if parent_id:
            try:
                parent_category = CategoryModel.objects.get(id=parent_id)
                attrs['parent'] = parent_category
            except CategoryModel.DoesNotExist:
                raise serializers.ValidationError("Parent category does not exist.")
        
        category_image_id = attrs.get('category_image_id')
        if category_image_id:
            try:
                category_image = ImageModel.objects.get(id=category_image_id)
                attrs['category_image'] = category_image
            except ImageModel.DoesNotExist:
                raise serializers.ValidationError("Category image does not exist.")
        
        category_icon_id = attrs.get('category_icon_id')
        if category_icon_id:
            try:
                category_icon = ImageModel.objects.get(id=category_icon_id)
                attrs['category_icon'] = category_icon
            except ImageModel.DoesNotExist:
                raise serializers.ValidationError("Category icon does not exist.")

        return attrs

    def create(self, validated_data):
        category = CategoryModel.objects.create(
            created_by=self.context['request'].user, 
            **validated_data
        )
        category.save()
        return category