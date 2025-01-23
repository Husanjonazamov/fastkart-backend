from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AttributeModel, AttributevalueModel


class AttributeValueInline(admin.TabularInline):
    model = AttributevalueModel
    extra = 1    

@admin.register(AttributeModel)
class AttributeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [AttributeValueInline]


@admin.register(AttributevalueModel)
class AttributevalueAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
