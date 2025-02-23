from rest_framework import serializers
from ...models import ProductModel
from core.apps.content.serializers.image import ListImageSerializer
from core.apps.product.serializers.category import ListCategorySerializer
from core.apps.product.serializers.tags import ListTagsSerializer
from core.apps.product.serializers.store import ListStoreSerializer
from core.apps.product.serializers.product.tax import TaxSerializer
from core.apps.product.serializers.attribute.attribute import ListAttributeSerializer
from core.apps.product.serializers.variation.variation import ListVariationSerializer





class BaseProductSerializer(serializers.ModelSerializer):
    product_thumbnail_id = serializers.SerializerMethodField()
    product_meta_image_id = serializers.SerializerMethodField()
    size_chart_image_id = serializers.SerializerMethodField()
    store_id = serializers.SerializerMethodField()
    created_by_id = serializers.SerializerMethodField()
    tax_id = serializers.SerializerMethodField()
    
    product_thumbnail = ListImageSerializer(required=False)
    product_meta_image = ListImageSerializer(required=False)
    size_chart_image = ListImageSerializer(required=False)
    product_galleries = ListImageSerializer(required=False, many=True)
    attributes = ListAttributeSerializer(required=False, many=True)
    variations = ListAttributeSerializer(required=False, many=True)
    
    store = ListStoreSerializer(required=False)
    tax = TaxSerializer(required=False)
    categories = ListCategorySerializer(required=False, many=True)
    tags = ListTagsSerializer(required=False, many=True)
    
    # Convert Boolean fields to 1 or 0
    is_featured = serializers.SerializerMethodField()
    is_cod = serializers.SerializerMethodField()
    is_free_shipping = serializers.SerializerMethodField()
    is_sale_enable = serializers.SerializerMethodField()
    is_return = serializers.SerializerMethodField()
    is_trending = serializers.SerializerMethodField()
    is_approved = serializers.SerializerMethodField()
    is_random_related_products = serializers.SerializerMethodField()
    safe_checkout = serializers.SerializerMethodField()
    secure_checkout = serializers.SerializerMethodField()
    social_share = serializers.SerializerMethodField()
    encourage_order = serializers.SerializerMethodField()
    encourage_view = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    can_review = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "description",
            "type",
            "unit",
            "weight",
            "quantity",
            "price",
            "sale_price",
            "discount",
            "is_featured",
            "shipping_days",
            "is_cod",
            "is_free_shipping",
            "is_sale_enable",
            "is_return",
            "is_trending",
            "is_approved",
            "sale_starts_at",
            "sale_expired_at",
            "sku",
            "is_random_related_products",
            "stock_status",
            "meta_title",
            "meta_description",
            "product_thumbnail_id",
            "product_meta_image_id",
            "size_chart_image_id",
            "estimated_delivery_text",
            "return_policy_text",
            "safe_checkout",
            "secure_checkout",
            "social_share",
            "encourage_order",
            "encourage_view",
            "status",
            "store_id",
            "created_by_id",
            "tax_id",
            "deleted_at",
            "created_at",
            "updated_at",
            "orders_count",
            "reviews_count",
            "can_review",
            "rating_count",
            "order_amount",
            "review_ratings",
            "related_products",
            "cross_sell_products",
            "product_thumbnail",
            "product_galleries",
            "product_meta_image",
            "size_chart_image",
            "reviews",
            "store",
            "tax",
            "categories",
            "tags",
            'attributes',
            'variations'
        ]

    def get_product_thumbnail_id(self, obj: ProductModel) -> int | None:
        return obj.product_thumbnail.id if obj.product_thumbnail else None

    def get_product_meta_image_id(self, obj: ProductModel) -> int | None:
        return obj.product_meta_image.id if obj.product_meta_image else None

    def get_size_chart_image_id(self, obj: ProductModel) -> int | None:
        return obj.size_chart_image.id if obj.size_chart_image else None

    def get_store_id(self, obj: ProductModel) -> int | None:
        return obj.store.id if obj.store else None

    def get_created_by_id(self, obj: ProductModel) -> int | None:
        return obj.created_by.id if obj.created_by else None

    def get_tax_id(self, obj: ProductModel) -> int | None:
        return obj.tax.id if obj.tax else None

    # Convert boolean fields to 1 or 0
    def get_is_featured(self, obj: ProductModel) -> int:
        return 1 if obj.is_featured else 0

    def get_is_cod(self, obj: ProductModel) -> int:
        return 1 if obj.is_cod else 0

    def get_is_free_shipping(self, obj: ProductModel) -> int:
        return 1 if obj.is_free_shipping else 0

    def get_is_sale_enable(self, obj: ProductModel) -> int:
        return 1 if obj.is_sale_enable else 0

    def get_is_return(self, obj: ProductModel) -> int:
        return 1 if obj.is_return else 0

    def get_is_trending(self, obj: ProductModel) -> int:
        return 1 if obj.is_trending else 0

    def get_is_approved(self, obj: ProductModel) -> int:
        return 1 if obj.is_approved else 0

    def get_is_random_related_products(self, obj: ProductModel) -> int:
        return 1 if obj.is_random_related_products else 0

    def get_safe_checkout(self, obj: ProductModel) -> int:
        return 1 if obj.safe_checkout else 0

    def get_secure_checkout(self, obj: ProductModel) -> int:
        return 1 if obj.secure_checkout else 0

    def get_social_share(self, obj: ProductModel) -> int:
        return 1 if obj.social_share else 0

    def get_encourage_order(self, obj: ProductModel) -> int:
        return 1 if obj.encourage_order else 0

    def get_encourage_view(self, obj: ProductModel) -> int:
        return 1 if obj.encourage_view else 0

    def get_status(self, obj: ProductModel) -> int:
        return 1 if obj.status else 0

    def get_can_review(self, obj: ProductModel) -> int:
        return 1 if obj.can_review else 0


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...
