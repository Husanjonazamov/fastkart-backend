from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import PaymentaccountModel


@admin.register(PaymentaccountModel)
class PaymentaccountAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
