from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import TaxModel


@admin.register(TaxModel)
class TaxAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
