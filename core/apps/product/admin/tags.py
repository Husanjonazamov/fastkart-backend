from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import TagsModel


@admin.register(TagsModel)
class TagsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
