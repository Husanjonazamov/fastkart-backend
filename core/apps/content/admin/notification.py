from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import NotificationdataModel, NotificationModel


@admin.register(NotificationdataModel)
class NotificationdataAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(NotificationModel)
class NotificationAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
