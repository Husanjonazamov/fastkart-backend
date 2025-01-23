from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TransactionModel(AbstractBaseModel):
    wallet = models.ForeignKey(
        "core.WalletsModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions",
    )
    order = models.ForeignKey(
        "orders.OrderModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions"
    )
    point = models.ForeignKey(
        "cart.PointsModel", on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)
    detail = models.TextField()
    from_user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Transaction"
        verbose_name = _("TransactionModel")
        verbose_name_plural = _("TransactionModels")
