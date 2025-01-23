from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import QuestionsModel


@admin.register(QuestionsModel)
class QuestionsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
