from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CartModel(AbstractBaseModel):
    product = models.ForeignKey(
        'product.ProductModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='carts'
    )
    variations = models.ForeignKey(
        'product.VariationModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    consumer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, blank=True)
    uantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Cart {self.id} for consumer {self.consumer}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Cart"
        verbose_name = _("CartModel")
        verbose_name_plural = _("CartModels")
