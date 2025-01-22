from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AttributeModel, AttributevalueModel


@admin.register(AttributeModel)
class AttributeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(AttributevalueModel)
class AttributevalueAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
