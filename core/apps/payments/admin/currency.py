from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CurrencyModel


@admin.register(CurrencyModel)
class CurrencyAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
