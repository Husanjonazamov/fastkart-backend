from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CouponModel


@admin.register(CouponModel)
class CouponAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
