from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CountryModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    currency = models.CharField(max_length=100)
    currency_symbol = models.CharField(max_length=10)
    iso_3166_2 = models.CharField(max_length=2)
    iso_3166_3 = models.CharField(max_length=3)
    calling_code = models.CharField(max_length=10)
    flag = models.CharField(max_length=255, null=True, blank=True)
    
    
    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "country"
        verbose_name = _("CountryModel")
        verbose_name_plural = _("CountryModels")
