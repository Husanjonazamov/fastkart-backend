from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import WishlistitemModel, WishlistModel


@admin.register(WishlistModel)
class WishlistAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(WishlistitemModel)
class WishlistitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
