from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class AddressModel(AbstractBaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name="address")
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)
    country_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    country = models.ForeignKey('address.CountryModel', on_delete=models.SET_NULL, null=True, blank=True, related_name="addresses")
    state = models.ForeignKey('address.StateModel', on_delete=models.SET_NULL, null=True, blank=True, related_name="addresses")
    

    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Address"
        verbose_name = _("AddressModel")
        verbose_name_plural = _("AddressModels")
