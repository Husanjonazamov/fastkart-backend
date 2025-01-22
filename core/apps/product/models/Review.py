from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ReviewModel(AbstractBaseModel):
    product = models.ForeignKey('product.ProductModel', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    consumer = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    store = models.ForeignKey('product.StoreModel', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    review_image = models.ForeignKey('content.ImageModel', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Review {self.pk} for Product {self.product}'

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Review"
        verbose_name = _("ReviewModel")
        verbose_name_plural = _("ReviewModels")
