from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.utils.text import slugify



class StoreModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=20)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    hide_vendor_email = models.BooleanField(default=False)
    hide_vendor_phone = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stores_created",
    )
    status = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    orders_count = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=0)
    products_count = models.IntegerField(default=0)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rating_count = models.IntegerField(default=0)
    store_logo = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="store_logos",
    )
    store_cover = models.ForeignKey(
        "content.ImageModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="store_covers",
    )
    vendor = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stores",
    )
    country = models.ForeignKey(
        "address.CountryModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stores",
    )
    state = models.ForeignKey(
        "address.StateModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stores",
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Store"
        verbose_name = _("StoreModel")
        verbose_name_plural = _("StoreModels")
