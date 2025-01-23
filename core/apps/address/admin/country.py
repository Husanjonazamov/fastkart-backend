from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CountryModel


@admin.register(CountryModel)
class CountryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
