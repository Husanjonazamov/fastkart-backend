from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ImageModel(AbstractBaseModel):
    collection_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    conversions_disk = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    created_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    original_url = models.URLField(max_length=200)

    def __str__(self):
        return self.file_name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Image"
        verbose_name = _("ImageModel")
        verbose_name_plural = _("ImageModel")
