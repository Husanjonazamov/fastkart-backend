from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CartModel


@admin.register(CartModel)
class CartAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
