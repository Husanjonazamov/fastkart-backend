from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class WishlistModel(AbstractBaseModel):
    consumer = models.OneToOneField('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name="wishlist")
    total = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.consumer}\'s wishlist {self.total} products'

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Wishlist"
        verbose_name = _("WishlistModel")
        verbose_name_plural = _("WishlistModels")


class WishlistitemModel(AbstractBaseModel):
    wishlist = models.ForeignKey(WishlistModel, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        "product.ProductModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="Wishlist_items",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product.name if self.product else f"Wishlist Item #{self.id}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "WishlistItem"
        verbose_name = _("WishlistitemModel")
        verbose_name_plural = _("WishlistitemModels")
