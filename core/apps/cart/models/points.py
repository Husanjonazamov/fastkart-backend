from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class PointsModel(AbstractBaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="point")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Point {self.pk}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Points"
        verbose_name = _("PointsModel")
        verbose_name_plural = _("PointsModels")
