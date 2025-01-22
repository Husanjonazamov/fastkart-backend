from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
