from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import TransactionModel


@admin.register(TransactionModel)
class TransactionAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
