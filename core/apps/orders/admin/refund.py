from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import RefundModel


@admin.register(RefundModel)
class RefundAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
