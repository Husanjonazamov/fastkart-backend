from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AddressModel


@admin.register(AddressModel)
class AddressAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
