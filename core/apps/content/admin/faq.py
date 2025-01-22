from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import FaqModel


@admin.register(FaqModel)
class FaqAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
