from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class SymbolPosition(models.TextChoices):
    BEFORE_PRICE = "before_price", "Before"
    AFTER_PRICE = "after_price", "After"
    
    
    
class ThousandsSeparator(models.TextChoices):
    COMMA = "comma", "Comma"
    DOT = "dot", "Dot"
    
    

class CurrencyModel(AbstractBaseModel):
    code = models.CharField(_("code"), max_length=10)
    symbol = models.CharField(max_length=10)
    no_of_decimal = models.IntegerField()
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)
    symbol_position = models.CharField(max_length=20, choices=SymbolPosition.choices)
    thousands_separator = models.CharField(max_length=10, choices=ThousandsSeparator.choices)
    decimal_separator = models.CharField(max_length=10)
    system_reserve = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey("accounts.User", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.code

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Currency"
        verbose_name = _("CurrencyModel")
        verbose_name_plural = _("CurrencyModels")
