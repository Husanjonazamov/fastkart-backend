from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class WalletType(models.TextChoices):
    consumer = "consumer", "Consumer"
    vendor = "vendor", "Vendor"


class WalletsModel(AbstractBaseModel):
    type = models.CharField(max_length=255, choices=WalletType.choices, default="consumer")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Wallet {self.pk} for consumer with balance {self.balance}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Wallet"
        verbose_name = _("WalletModel")
        verbose_name_plural = _("WalletModels")
