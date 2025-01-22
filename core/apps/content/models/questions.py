from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class QuestionModel(AbstractBaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    consumer = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    product = models.ForeignKey('product.ProductModel', on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    reaction = models.CharField(max_length=255, null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    total_dislikes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question[:30]

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Question"
        verbose_name = _("QuestionModel")
        verbose_name_plural = _("QuestionModels")
