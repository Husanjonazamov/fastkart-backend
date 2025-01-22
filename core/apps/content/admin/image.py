from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import ImageModel


@admin.register(ImageModel)
class ImageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
