from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver




class OrderstatusModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    sequence = models.IntegerField()
    created_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    system_reserve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "OrderStatus"
        verbose_name = _("OrderstatusModel")
        verbose_name_plural = _("OrderstatusModels")


class PaymentMethodChoices(models.TextChoices):
    PAYPAL = "paypal", "Paypal"
    STRIPE = "stripe", "Stripe"
    RAZORPAY = "razorpay", "Razorpay"
    COD = "cod", "Cod"
    WALLET = "wallet", "Wallet"
    POINTS = "points", "Points"


class PaymentStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    COMPLETED = "completed", "Completed"
    REFUNDED = "refunded", "Refunded"
    CANCELLED = "cancelled", "Cancelled"
    FAILED = "failed", "Failed"
    PARTIALLY_REFUNDED = "partially_refunded", "Partially Refunded"





class OrderModel(AbstractBaseModel):
    order_number = models.IntegerField(unique=True, null=True, blank=True)
    consumer = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, blank=True)
    tax_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    points_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_total_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(
        max_length=50, choices=PaymentMethodChoices.choices
    )
    payment_status = models.CharField(
        max_length=50, choices=PaymentStatusChoices.choices
    )
    delivery_description = models.CharField(max_length=255)
    delivery_interval = models.CharField(max_length=255, null=True, blank=True)
    order_status = models.ForeignKey(OrderstatusModel, on_delete=models.CASCADE)
    coupon = models.ForeignKey(
        "cart.CouponModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="sub_orders",
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    invoice_url = models.URLField(max_length=200, blank=True)
    status = models.BooleanField(default=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    store = models.ForeignKey(
        "product.StoreModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    products = models.ManyToManyField("product.ProductModel")
    billing_address = models.ForeignKey(
        "orders.AddressModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_billings",
    )
    shipping_address = models.ForeignKey(
        "orders.AddressModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_shippings",
    )

    def __str__(self):
        return f"Order {self.order_number}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")
