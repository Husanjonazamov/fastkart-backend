from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class StateModel(AbstractBaseModel):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        'core.CountryModel', on_delete=models.CASCADE, related_name="states"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "State"
        verbose_name = _("StateModel")
        verbose_name_plural = _("StateModels")
