from ..models import VariationModel
from unfold.admin import ModelAdmin
from django.contrib import admin


@admin.register(VariationModel)
class VariationAdmin(ModelAdmin):
    list_display = ("id", "__str__",)
