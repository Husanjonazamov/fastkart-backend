from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.utils.text import slugify



class TYPE_CHOICES(models.TextChoices):
    BLOG = "blog", "Blog"
    PRODUCT = "product", "Product"
    BOTH = "both", "Both"
    POST = 'post', 'Post'


class CategoryModel(AbstractBaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES.choices)
    commission_rate = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="categories",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    blogs_count = models.IntegerField(default=0)
    products_count = models.IntegerField(default=0)
    category_image = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category_images",
    )
    category_icon = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category_icons",
    )
    subcategories = models.ManyToManyField(
        "CategoryModel", symmetrical=False, related_name="parent_category", blank=True
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )


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
        db_table = "Category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")
