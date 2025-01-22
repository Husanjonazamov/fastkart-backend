from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import OrderModel, OrderstatusModel


@admin.register(OrderstatusModel)
class OrderstatusAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
