from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import StoreModel


@admin.register(StoreModel)
class StoreAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
