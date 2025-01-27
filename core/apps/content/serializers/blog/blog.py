from rest_framework import serializers

from ...models import BlogModel
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.product.serializers.tags import ListTagsSerializer


class BaseBlogSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.IntegerField(source="created_by.id", read_only=True)
    blog_thumbnail_id = serializers.SerializerMethodField()
    blog_thumbnail = ListImageSerializer(read_only=True)
    blog_meta_image_id = serializers.SerializerMethodField()
    blog_meta_image = ListImageSerializer(read_only=True)
    tags = ListTagsSerializer(many=True, read_only=True)
    categories = serializers.SerializerMethodField()
    
    is_featured = serializers.SerializerMethodField()
    is_sticky = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    

   

    class Meta:
        model = BlogModel
        fields = [
            "title",
            "slug",
            "descriptions",
            "content",
            "meta_title",
            "blog_thumbnail_id",
            "meta_description",
            "blog_meta_image_id",
            "is_featured",
            "is_sticky",
            "status",
            "created_by_id",
            "created_at",
            "updated_at",
            "deleted_at",
            "blog_thumbnail",
            "blog_meta_image",
            "categories",
            "created_by",
            "tags",
        ]
        read_only_fields = [
            "slug",
            "created_by_id",
            "created_by",
            "blog_thumbnail",
            "blog_meta_image",
            "created_at",
            "updated_at",
            "deleted_at",
        ]
        
    def get_categories(self, obj: BlogModel):
        from core.apps.product.serializers.category import ListCategorySerializer
        return ListCategorySerializer(obj.categories.all(), many=True).data
    

    def get_is_featured(self, obj: BlogModel):
            return 1 if obj.is_featured else 0

    def get_is_sticky(self, obj: BlogModel):
        return 1 if obj.is_sticky else 0

    def get_status(self, obj: BlogModel):
        return 1 if obj.status else 0


    def get_blog_thumbnail_id(self, obj: BlogModel) -> int | None:
        return obj.blog_thumbnail.id if obj.blog_thumbnail else None

    def get_blog_meta_image_id(self, obj: BlogModel) -> int | None:
        return obj.blog_meta_image.id if obj.blog_meta_image else None


class ListBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...


class RetrieveBlogSerializer(BaseBlogSerializer):
    class Meta(BaseBlogSerializer.Meta): ...


class CreateBlogSerializer(BaseBlogSerializer):
    created_by_id = serializers.IntegerField(write_only=True)

    class Meta(BaseBlogSerializer.Meta):
        fields = BaseBlogSerializer.Meta.fields + ["created_by_id"]

    def create(self, validated_data):
        user = self.context['request'].user

        if user.is_anonymous:
            raise serializers.ValidationError("Foydalanuvchi tizimga kirgan bo'lishi kerak.")
        
        validated_data['created_by'] = user 

        blog = BlogModel.objects.create(**validated_data)

        tags_data = validated_data.pop('tags', [])
        categories_data = validated_data.pop('categories', [])

        if tags_data:
            blog.tags.set(tags_data)

        if categories_data:
            blog.categories.set(categories_data)

        return blog

