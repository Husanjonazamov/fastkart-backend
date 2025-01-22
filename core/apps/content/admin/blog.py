from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BlogModel, ImageModel


@admin.register(BlogModel)
class BlogAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ImageModel)
class ImageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
