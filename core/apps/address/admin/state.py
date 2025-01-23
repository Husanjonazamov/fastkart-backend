from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import StateModel


@admin.register(StateModel)
class StateAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
