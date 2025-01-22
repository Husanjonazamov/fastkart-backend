from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class AttributeModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    style = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
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
        db_table = "Attribute"
        verbose_name = _("AttributeModel")
        verbose_name_plural = _("AttributeModels")



class AttributevalueModel(AbstractBaseModel):
    attribute = models.ForeignKey(AttributeModel, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    hex_color = models.CharField(max_length=10, null=True, blank=True)
    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.attribute.name}"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "AttributeValue"
        verbose_name = _("AttributevalueModel")
        verbose_name_plural = _("AttributevalueModels")
