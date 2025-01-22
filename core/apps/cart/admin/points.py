from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import PointsModel


@admin.register(PointsModel)
class PointsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
