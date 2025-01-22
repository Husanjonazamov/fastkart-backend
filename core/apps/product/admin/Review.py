from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import ReviewModel


@admin.register(ReviewModel)
class ReviewAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
