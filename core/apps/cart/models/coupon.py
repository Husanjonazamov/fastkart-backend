from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class CouponType(models.TextChoices):
    PERCENTAGE = "percentage", "Percentage"
    FIXED = "fixed", "Fixed"
    

class CouponModel(AbstractBaseModel):
    title = models.CharField(_("name"), max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=100, choices=CouponType.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    min_spend = models.DecimalField(max_digits=10, decimal_places=2)
    is_unlimited = models.BooleanField(default=False)
    usage_per_coupon = models.IntegerField(default=0)
    usage_per_customer = models.IntegerField(default=1)
    used = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    is_expired = models.BooleanField(default=False)
    is_apply_all = models.BooleanField(default=True)
    is_first_order = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='coupons')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Coupon"
        verbose_name = _("CouponModel")
        verbose_name_plural = _("CouponModels")
