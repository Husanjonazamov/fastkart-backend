from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
import uuid

class NotificationDataTypes(models.TextChoices):
    ORDER = "order", "Order"
    PAYMENT = "payment", "Payment"
    REFUND = "refund", "Refund"
    COUPON = "coupon", "Coupon"



class NotificationdataModel(AbstractBaseModel):
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=255, choices=NotificationDataTypes.choices)

    def __str__(self):
        return self.title

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "NotificationData"
        verbose_name = _("NotificationdataModel")
        verbose_name_plural = _("NotificationdataModels")



class NotificationModel(AbstractBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    notifiable_type = models.CharField(max_length=255)
    notifiable_id = models.IntegerField()
    data = models.ForeignKey(NotificationdataModel, on_delete=models.CASCADE)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Notification"
        verbose_name = _("NotificationModel")
        verbose_name_plural = _("NotificationModels")
