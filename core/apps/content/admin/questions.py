from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import QuestionModel


@admin.register(QuestionModel)
class QuestionAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
