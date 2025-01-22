from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CompareitemModel, CompareModel


@admin.register(CompareModel)
class CompareAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CompareitemModel)
class CompareitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
