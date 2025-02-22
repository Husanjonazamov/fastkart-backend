from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class StockStatusChoices(models.TextChoices):
    IN_STOCK = 'in_stock', _('In Stock')
    OUT_OF_STOCK = 'out_of_stock', _('Out of Stock')
    ON_BACKORDER = 'on_backorder', _('On Backorder')

class ProductTypeChoices(models.TextChoices):
    SIMPLE = "simple", _("Simple product")
    VARIABLE = "variable", _("Product with variations")
    GROUPED = "grouped", _("Collection of products")
    EXTERNAL = "external", _("External product")
    AFFILIATE = "affiliate", _("Affiliate product")
    VIRTUAL = "virtual", _("Virtual product")
    DOWNLOADABLE = "downloadable", _("Downloadable product")

    
class ProductModel(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=ProductTypeChoices.choices)
    unit = models.CharField(max_length=100)
    weight = models.FloatField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    shipping_days = models.PositiveIntegerField(null=True, blank=True)
    is_cod = models.BooleanField(default=False)
    is_free_shipping = models.BooleanField(default=False)
    is_sale_enable = models.BooleanField(default=False)
    is_return = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    sale_starts_at = models.DateTimeField(null=True, blank=True)
    sale_expired_at = models.DateTimeField(null=True, blank=True)
    sku = models.CharField(max_length=255, unique=True)
    is_random_related_products = models.BooleanField(default=False)
    stock_status = models.CharField(
        max_length=50,
        choices=StockStatusChoices.choices,
        default=StockStatusChoices.IN_STOCK,
    )
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    product_thumbnail = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product_thumbnails",
    )
    product_meta_image = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product_meta_images",
    )
    size_chart_image = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="size_chart_images",
    )
    estimated_delivery_text = models.CharField(max_length=255, null=True, blank=True)
    return_policy_text = models.CharField(max_length=255, null=True, blank=True)
    safe_checkout = models.BooleanField(default=False)
    secure_checkout = models.BooleanField(default=False)
    social_share = models.BooleanField(default=False)
    encourage_order = models.BooleanField(default=False)
    encourage_view = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)
    store = models.ForeignKey(
        "product.StoreModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    created_by = models.ForeignKey(
        'accounts.User', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="products"
    )
    tax = models.ForeignKey(
        'product.TaxModel', on_delete=models.SET_NULL, null=True, blank=True
    )
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    orders_count = models.PositiveIntegerField(default=0)
    reviews_count = models.PositiveIntegerField(default=0)
    can_review = models.BooleanField(default=True)
    rating_count = models.FloatField(default=0.0)
    order_amount = models.FloatField(default=0.0)
    review_ratings = models.JSONField(default=list, blank=True)
    related_products = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="related_to_products"
    )
    cross_sell_products = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="cross_sells"
    )
    product_galleries = models.ManyToManyField("content.ImageModel", blank=True, related_name="product_galleries")
    categories = models.ManyToManyField("product.CategoryModel", blank=True, related_name="products")
    tags = models.ManyToManyField("product.TagsModel", blank=True, related_name="products")
    attributes = models.ManyToManyField("product.AttributeModel", blank=True, related_name="products")
    variations = models.ManyToManyField("product.VariationModel", blank=True, related_name="products")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.review_ratings:
            self.review_ratings = [0, 0, 0, 0, 0]
        super().save(*args, **kwargs)

    class Meta:
        db_table = "product"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
