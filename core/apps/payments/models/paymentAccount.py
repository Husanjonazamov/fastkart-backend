from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class PaymentaccountModel(AbstractBaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.SET_NULL, null=True, blank=True, related_name='payment_account')
    paypal_email = models.EmailField(null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    bank_holder_name = models.CharField(max_length=255, null=True, blank=True)
    bank_account_no = models.CharField(max_length=255, null=True, blank=True)
    swift = models.CharField(max_length=255, null=True, blank=True)
    ifsc = models.CharField(max_length=255, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"PaymentAccount {self.pk} for user {self.user}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "PaymentAccount"
        verbose_name = _("PaymentaccountModel")
        verbose_name_plural = _("PaymentaccountModels")
