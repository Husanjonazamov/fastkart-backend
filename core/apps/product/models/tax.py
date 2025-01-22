from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TaxModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name="taxes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Tax"
        verbose_name = _("TaxModel")
        verbose_name_plural = _("TaxModels")
