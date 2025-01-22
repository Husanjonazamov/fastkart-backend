from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import WalletModel


@admin.register(WalletModel)
class WalletAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
