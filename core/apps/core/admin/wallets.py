from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import WalletsModel


@admin.register(WalletsModel)
class WalletsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
