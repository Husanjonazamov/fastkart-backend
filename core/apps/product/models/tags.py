from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TYPE_CHOICES(models.TextChoices):
    BLOG = "blog", "Blog"
    POST = "post", "Post"
    PRODUCT = "product", "Product"
    CATEGORY = "category", "Category"
    BRAND = "brand", "Brand"
    SIZE = "size", "Size"
    COLOR = "color", "Color"


class TagsModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    slug = models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES.choices)
    descriptions = models.TextField()
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    blogs_count = models.IntegerField(default=0)
    products_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Tags"
        verbose_name = _("TagsModel")
        verbose_name_plural = _("TagsModels")


