from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from core.apps.orders.models import PaymentStatusChoices

class RefaundPaymentType(models.TextChoices):
    CASH = 'cash', "Cash"
    BANK = 'bank', "Bank"
    PAYPAL = 'paypal', "Paypal"
    STRIPE = 'stripe', "Stripe"
    CREDIT_CARD = 'credit_card', "Credit Card"
    DEBIT_CARD = 'debit_card', "Debit Card"
    MOBILE_MONEY = 'mobile_money', "Mobile Money"
    OTHER = 'other', "Other"



class RefundModel(AbstractBaseModel):
    reason = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    store = models.ForeignKey('product.StoreModel', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey('orders.OrderModel', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('product.ProductModel', on_delete=models.SET_NULL, null=True, blank=True)
    consumer = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    variation = models.ForeignKey('product.VariationModel', on_delete=models.SET_NULL, null=True, blank=True)
    refund_image = models.ForeignKey('content.ImageModel', on_delete=models.SET_NULL, null=True, blank=True)
    payment_type = models.CharField(max_length=50, choices=RefaundPaymentType.choices)
    status = models.CharField(max_length=50, choices=PaymentStatusChoices.choices)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Refund {self.id} - {self.status}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Refund"
        verbose_name = _("RefundModel")
        verbose_name_plural = _("RefundModels")
