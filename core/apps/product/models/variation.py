from django.db import models
from django_core.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _
from core.apps.product.models.product import StokcStatusChoices


class VariationModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    stock_status = models.CharField(max_length=50, choices=StokcStatusChoices.choices)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    sku = models.CharField(max_length=50)
    status = models.IntegerField()
    variation_options = models.JSONField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    variation_image = models.ImageField(upload_to='variations/', null=True, blank=True)
    attribute_values = models.ManyToManyField('product.AttributevalueModel', related_name='variations')

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Variation "
        verbose_name = _("Variation Model")
        verbose_name_plural = _("Variation Models")
