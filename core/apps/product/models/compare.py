from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CompareModel(AbstractBaseModel):
    consumer = models.OneToOneField('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.consumer}\'s compare {self.total} products'

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Compare"
        verbose_name = _("CompareModel")
        verbose_name_plural = _("CompareModels")


class CompareitemModel(AbstractBaseModel):
    compare = models.ForeignKey(CompareModel, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        "product.ProductModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="compare_items",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.compare.consumer}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "CompareItem"
        verbose_name = _("CompareitemModel")
        verbose_name_plural = _("CompareitemModels")
